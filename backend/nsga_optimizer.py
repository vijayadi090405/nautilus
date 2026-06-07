import numpy as np

from pymoo.core.problem import Problem

from pymoo.algorithms.moo.nsga2 import NSGA2

from pymoo.optimize import minimize

from physics import (
        drag_force,
        hydrodynamic_efficiency
    )
from acoustics import source_level
from sonar import (
    signal_excess,
    detection_probability
)
from structure import safety_factor
from materials import MATERIALS
from target import target_strength

from environment import (
    ambient_noise,
    directivity_index,
    detection_threshold
)

class TorpedoOptimizationProblem(
    Problem
):

    def __init__(
        self,
        target_range,
        depth,
        stealth_priority,
        mission_type
    ):

        self.target_range = target_range
        self.depth = depth
        self.stealth_priority = stealth_priority
        self.mission_type = mission_type
        super().__init__(
            n_var=4,
            n_obj=4,
            n_constr=0,
            xl=np.array([
                0.35,
                3.0,
                30,
                0
            ]),
            xu=np.array([
                1.2,
                10.0,
                80,
                2
            ])
        )

    def _evaluate(
        self,
        X,
        out,
        *args,
        **kwargs
    ):

        F = []

        for row in X:

            diameter = row[0]
            length = row[1]
            speed = row[2]

            material_index = int(
                round(row[3])
            )

            materials = [
                "Steel",
                "Titanium",
                "Composite"
            ]

            material = materials[
                material_index
            ]

            propulsion_map = {
                "Steel":
                "Thermal",

                "Titanium":
                "Pump-Jet",

                "Composite":
                "Electric"
            }

            propulsion = propulsion_map[
                material
            ]

            drag = drag_force(
                diameter,
                length,
                speed
            )

            hydro_eff = hydrodynamic_efficiency(
                diameter,
                length,
                speed
            )
            ld_ratio = (
                length /
                max(diameter, 0.01)
            )
            sl = source_level(
                propulsion,
                speed
            )

            ts = target_strength(
                diameter,
                length
            )

            nl = ambient_noise(
                3
            )

            di = directivity_index()

            dt = detection_threshold()

            se = signal_excess(

                source_level=sl,

                distance_km=5,

                target_strength=ts,

                ambient_noise=nl,

                directivity_index=di,

                detection_threshold=dt

            )

            detection = detection_probability(
                se
            )

            energy_factor = {

                "Electric": 1.0,
                "Pump-Jet": 1.6,
                "Thermal": 2.2

            }[propulsion]

            estimated_range = (
                (
                    length *
                    speed *
                    energy_factor
                )
                /
                (
                    drag / 1000 + 1
                )
            )

            range_error = abs(
                self.target_range
                -
                estimated_range
            )

            depth_m = (
                2000
                if self.depth ==
                "Deep"
                else 500
            )

            props = MATERIALS[
                material
            ]

            sf = safety_factor(

                props["yield"],

                props["youngs_modulus"],

                props["poisson"],

                depth_m,

                hull_radius_m=
                diameter / 2,

                hull_thickness_m=
                diameter * 0.03

            )

            survivability = min(
                100,
                (sf / 4) * 100
            )

            if self.stealth_priority == "High":

                detection_weight = 2.0

            elif self.stealth_priority == "Medium":

                detection_weight = 1.0

            else:

                detection_weight = 0.5


            if self.mission_type == "Anti-Submarine":

                F.append([
                    detection * detection_weight * 2,
                    range_error,
                    -(survivability + hydro_eff + ld_ratio),
                    drag
                ])

            elif self.mission_type == "Deep Strike":

                F.append([
                    detection * detection_weight,
                    range_error * 2,
                    -(survivability + hydro_eff + ld_ratio),
                    drag
                ])          

            elif self.mission_type == "Coastal Defense":

                F.append([
                    detection * detection_weight,
                    range_error,
                    -(survivability * 1.5 + hydro_eff + ld_ratio),
                    drag
                ])

            else:

                F.append([
                    detection,
                    range_error,
                    -(survivability + hydro_eff + ld_ratio),
                    drag
                ])

        out["F"] = np.array(F)
        
def run_nsga(
    target_range,
    stealth_priority,
    depth,
    mission_type
):

    problem = (
        TorpedoOptimizationProblem(
            target_range,
            depth,
            stealth_priority,
            mission_type
        )
    )

    algorithm = NSGA2(
        pop_size=150
    )

    result = minimize(
        problem,
        algorithm,
        ('n_gen', 150),
        seed=None,
        verbose=False
    )

    return result