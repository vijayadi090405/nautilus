import math
import random

from physics import (
        drag_force,
        hydrodynamic_efficiency
    )
from acoustics import source_level
from sonar import signal_excess, detection_probability
from structure import safety_factor
from materials import MATERIALS
from nsga_optimizer import run_nsga
from target import (
    target_strength
)
from advisor_reasoning import (
    generate_advisor_reasoning
)
from environment import (

    ambient_noise,

    directivity_index,

    detection_threshold

)
from structure import (
    buckling_pressure,
    collapse_depth
)
from energy import (

    power_required,

    stored_energy,

    endurance_hours,

    mission_range_km

)
from signatures import (
    acoustic_index,
    magnetic_index,
    thermal_index
)



def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _normalize_priority(value) -> str:
    return str(value).strip().capitalize()


def _normalize_depth(value) -> str:
    return str(value).strip().capitalize()


def optimize_design(
    target_range,
    stealth_priority,
    depth,
    mission_type=None
):
    target_range = float(target_range)
    stealth_priority = _normalize_priority(stealth_priority)
    depth = _normalize_depth(depth)

    result = run_nsga(
        target_range,
        stealth_priority,
        depth,
        mission_type
    )

    candidates = []
    materials = [
        "Steel",
        "Titanium",
        "Composite"
    ]

    for row in result.X:

        diameter = round(
            float(row[0]),
            2
        )

        length = round(
            float(row[1]),
            2
        )

        speed = round(
            float(row[2]),
            2
        )

        material = materials[
            int(
                round(
                    row[3]
                )
            )
        ]
        propulsion_map = {
            "Steel": "Thermal",
            "Titanium": "Pump-Jet",
            "Composite": "Electric"
        }

        coating_map = {
            "Steel": "Standard",
            "Titanium": "Low-Noise",
            "Composite": "Anechoic"
        }

        propulsion = propulsion_map[
            material
        ]

        coating = coating_map[
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
        sl = source_level(
            propulsion,
            speed
        )

        ts = target_strength(
            diameter,
            length
        )

        nl = ambient_noise(3)

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
        acoustic_sig = acoustic_index(
            sl
        )

        magnetic_sig = magnetic_index(
            material
        )

        thermal_sig = thermal_index(
            propulsion
        )
        material_props = (
            MATERIALS[
                material
            ]
        )

        sf = safety_factor(

            material_props["yield"],

            material_props[
                "youngs_modulus"
            ],

            material_props[
                "poisson"
            ],

            2000 if depth=="Deep"
            else 500,

            hull_radius_m=
            diameter / 2,

            hull_thickness_m=
            diameter * 0.03

        )
        collapse_pressure_value = (
            buckling_pressure(
                material_props[
                    "youngs_modulus"
                ],
                material_props[
                    "poisson"
                ],
                diameter * 0.03,
                diameter / 2
            )
        )

        depth_rating = round(
            collapse_depth(
                collapse_pressure_value
            ),
            0
        )
        survivability = min(
            100,
            (sf/4)*100
        )

        volume = (
            3.14159
            *
            (diameter/2)**2
            *
            length
        )

        mass = round(
            volume
            *
            material_props[
                "density"
            ]
            *
            0.18,
            2
        )

        power = power_required(
            drag,
            speed
        )

        energy = stored_energy(
            propulsion,
            mass
        )

        endurance = endurance_hours(
            energy,
            power
        )

        estimated_range = mission_range_km(
            endurance,
            speed
        )

        if detection < 20:

            design_type = "Ultra Stealth"

        elif estimated_range > 500:

            design_type = "Long Range Strike"

        elif speed > 70:

            design_type = "Rapid Interceptor"

        elif survivability > 90:

            design_type = "Deep Ocean Hunter"

        else:

            design_type = "Balanced Multirole"

        if mission_type == "Anti-Submarine":

            mission_score = (
                (100 - detection) * 0.55
                +
                survivability * 0.25
                +
                min(estimated_range,100) * 0.20
            )

        elif mission_type == "Coastal Defense":

            mission_score = (
                survivability * 0.45
                +
                min(estimated_range,100) * 0.35
                +
                (100 - detection) * 0.20
            )

        elif mission_type == "Deep Strike":

            mission_score = (
                min(estimated_range,100) * 0.55
                +
                survivability * 0.25
                +
                (100 - detection) * 0.20
            )

        else:

            mission_score = (
                (100-detection)*0.40
                +
                survivability*0.35
                +
                min(estimated_range,100)*0.25
            )

        candidates.append({

            "diameter":
            diameter,

            "length":
            length,

            "speed":
            speed,

            "mass":
            mass,

            "material":
            material,

            "propulsion":
            propulsion,

            "coating":
            coating,

            "designType":
            design_type,

            "drag":
            round(
                drag,
                2
            ),

            "sourceLevel":
            round(
                sl,
                2
            ),

            "detection":
            round(
                detection,
                2
            ),

            "survivability":
            round(
                survivability,
                2
            ),

            "safetyFactor":
            round(
                sf,
                2
            ),

            "range":
            round(
                estimated_range,
                2
            ),

            "score":
            round(
                mission_score,
                2
            ),
            "depthRating":
depth_rating,

"powerRequired":
round(
    power/1000,
    2
),

"endurance":
round(
    endurance,
    2
),

"estimatedRange":
round(
    estimated_range,
    2
),

"targetStrength":
round(
    ts,
    2
),

"ambientNoise":
round(
    nl,
    2
),

"directivityIndex":
round(
    di,
    2
),

"detectionThreshold":
round(
    dt,
    2
),
"acousticSignature":
round(
    acoustic_sig,
    2
),

"magneticSignature":
round(
    magnetic_sig,
    2
),

"thermalSignature":
round(
    thermal_sig,
    2
),
"hydrodynamicEfficiency":
round(
    hydro_eff,
    2
),
"collapseDepth": depth_rating,

"bucklingSafetyFactor": round(
    sf,
    2
),
        })


    candidates.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    best_design = dict(
        candidates[0]
    )

    selection_reason = []

    selection_reason.append(
        f"Mission score {best_design['score']} was highest among all generated candidates."
    )

    selection_reason.append(
        f"Detection probability reduced to {best_design['detection']}%."
    )

    selection_reason.append(
        f"Estimated range achieved {best_design['estimatedRange']} km."
    )

    selection_reason.append(
        f"Survivability reached {best_design['survivability']}%."
    )

    # Generate diverse alternatives

    alternatives = []

    for candidate in candidates[1:]:

        speed_gap = abs(
            candidate["speed"]
            -
            best_design["speed"]
        )

        range_gap = abs(
            candidate["estimatedRange"]
            -
            best_design["estimatedRange"]
        )

        if speed_gap < 2 and range_gap < 20:
            continue

        alternatives.append(candidate)

        if len(alternatives) == 5:
            break

    # Remove duplicates

    unique_alternatives = []
    seen = set()

    for alt in alternatives:

        key = (
            alt["diameter"],
            alt["length"],
            alt["speed"],
            alt["material"]
        )

        if key not in seen:

            seen.add(key)

            unique_alternatives.append(
                alt
            )
    warnings = []

    if mission_type == "Anti-Submarine":

        if stealth_priority == "Low":

            warnings.append(
                "Low stealth is not recommended for anti-submarine missions."
            )

    if mission_type == "Deep Strike":

        if target_range < 50:

            warnings.append(
                "Deep strike missions typically require larger operational range."
            )

    if depth == "Deep":

        if best_design["material"] == "Steel":

            warnings.append(
                "Titanium or Composite hulls are generally preferred for deep operations."
            )

    category_winners = {

        "bestStealth":
        min(
            candidates,
            key=lambda x:
            x["detection"]
        ),

        "bestRange":
        max(
            candidates,
            key=lambda x:
            x["estimatedRange"]
        ),

        "bestSpeed":
        max(
            candidates,
            key=lambda x:
            x["speed"]
        ),

        "bestSurvivability":
        max(
            candidates,
            key=lambda x:
            x["survivability"]
        )
    }

    for candidate in candidates:

        candidate["reasoning"] = (
            generate_advisor_reasoning(
                candidate,
                mission_type
            )
        )

    best_design["reasoning"] = (
        generate_advisor_reasoning(
            best_design,
            mission_type
        )
    )

    return {

        "best":
        best_design,

        "alternatives":
        alternatives,

        "warnings":
        warnings,

        "categoryWinners":
        category_winners,

        "selectionReason":
        selection_reason,
    }
