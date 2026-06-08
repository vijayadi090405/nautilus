import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import TorpedoScene from "../components/TorpedoScene";
import MetricsPanel from "../components/MetricsPanel";
import SonarPanel from "../components/SonarPanel";

export default function DesignMode() {

  const navigate = useNavigate();
  const [diameter, setDiameter] = useState(0.5);
  const [length, setLength] = useState(4);
  
  const [speed, setSpeed] = useState(40);

  const [propulsion, setPropulsion] =
    useState("Electric");
  const [coating, setCoating] =
  useState("None");

const [material, setMaterial] =
  useState("Steel");

  const [metrics, setMetrics] =
    useState(null);

  useEffect(() => {

  console.log(
    "SIMULATION TRIGGERED"
  );

  const runSimulation = async () => {

    try {

      console.log(
        "SENDING REQUEST"
      );

      const response =
        await axios.post(
          "https://nautilus-lsmu.onrender.com/simulate",
          {
            diameter,
            length,
            speed,
            propulsion,
            material,
            coating
          }
        );

      console.log(
        "RESPONSE RECEIVED",
        response.data
      );

      setMetrics(
        response.data
      );

    }

    catch (err) {

      console.error(
        "SIMULATION FAILED",
        err
      );

    }

  };

  runSimulation();

}, [
  diameter,
  length,
  speed,
  propulsion,
  material,
  coating
]);

  return (
    <div className=" relative z-10 min-h-screen bg-slate-950 text-white">
<div className="design-grid" />

<div className="scan-line" />
      <div className="relative z-10 grid grid-cols-12 h-screen">

        {/* INPUT PANEL */}

        <div className="col-span-3 p-4 overflow-y-auto">

  <div className="glass-card p-6 h-full">

          <button
  onClick={() => navigate("/")}
  className="glass-button px-4 py-2 mb-6"
>
  ← Back
</button>
<div className="mb-4 text-xs uppercase tracking-widest text-cyan-300">
  Design Parameters
</div>

          <h1 className="text-3xl font-bold mb-8">
            Design & Simulate
          </h1>

          <div className="parameter-scroll overflow-y-auto max-h-[70vh] pr-2">

          <div className="mb-6">

            <label>Diameter</label>

            <input
              type="range"
              min="0.2"
              max="1.5"
              step="0.1"
              value={diameter}
              onChange={(e) =>
                setDiameter(
                  Number(e.target.value)
                )
              }
              className="w-full"
            />

            <p>{diameter} m</p>

          </div>

          <div className="mb-6">

            <label>Length</label>

            <input
              type="range"
              min="2"
              max="10"
              step="0.5"
              value={length}
              onChange={(e) =>
                setLength(
                  Number(e.target.value)
                )
              }
              className="w-full"
            />

            <p>{length} m</p>

          </div>

          <div className="mb-6">

            <label>Speed</label>

            <input
              type="range"
              min="10"
              max="80"
              step="1"
              value={speed}
              onChange={(e) =>
                setSpeed(
                  Number(e.target.value)
                )
              }
              className="w-full"
            />

            <p>{speed} knots</p>

          </div>

          <div className="mb-6">

            <label>Propulsion</label>

            <select
              value={propulsion}
              onChange={(e) =>
                setPropulsion(
                  e.target.value
                )
              }
              className="w-full p-2 bg-slate-800 rounded"
            >
              <option value="Electric">
                Electric
              </option>

              <option value="Thermal">
                Thermal
              </option>

              <option value="Pump-Jet">
                Pump-Jet
              </option>

            </select>

          </div>
          <div className="mb-6">

<label>Hull Material</label>

<select
  value={material}
  onChange={(e)=>
    setMaterial(e.target.value)
  }
  className="w-full p-2 bg-slate-800 rounded"
>

<option>Steel</option>

<option>Titanium</option>

<option>Composite</option>

</select>

</div>
<div className="mb-6">

<label>Anechoic Coating</label>

<select
  value={coating}
  onChange={(e)=>
    setCoating(e.target.value)
  }
  className="w-full p-2 bg-slate-800 rounded"
>

<option>None</option>

<option>Basic</option>

<option>Anechoic</option>

</select>

</div>
</div>
        </div>
  </div>

        {/* TORPEDO */}

        <div className="col-span-6 p-4">

          <div className="glass-card h-140 p-4 relative">

  <div className="mb-4 text-xs uppercase tracking-widest text-cyan-300">
    TACTICAL DIGITAL TWIN
  </div>
<div className="absolute inset-0 pointer-events-none">

  <div
    className="
      absolute
      left-1/2
      top-1/2
      w-[250px]
      h-[250px]
      border
      border-cyan-400/20
      rounded-full
      -translate-x-1/2
      -translate-y-1/2
    "
  />

  <div
    className="
      absolute
      left-1/2
      top-1/2
      w-[450px]
      h-[450px]
      border
      border-cyan-400/20
      rounded-full
      -translate-x-1/2
      -translate-y-1/2
    "
  />

  <div
    className="
      absolute
      left-1/2
      top-1/2
      w-[650px]
      h-[650px]
      border
      border-cyan-400/5
      rounded-full
      -translate-x-1/2
      -translate-y-1/2
    "
  />

</div>
  <TorpedoScene
  diameter={diameter}
  length={length}
  propulsion={propulsion}
  material={material}
  acousticSignature={
    metrics?.acousticSignature
  }
/>
          </div>
          
<div className="mt-4 grid grid-cols-2 gap-4">

  <div className="glass-card p-4">

    <div className="text-xs uppercase tracking-widest text-cyan-300 mb-2">
      Vehicle Parameters
    </div>

    <div className="text-sm space-y-1">
      <div>Diameter: {diameter} m</div>
      <div>Length: {length} m</div>
      <div>
Material: {material}
</div>
      <div>Propulsion: {propulsion}</div>
    </div>

  </div>

  {metrics && (

    <div className="glass-card p-4">

      <div className="text-xs uppercase tracking-widest text-cyan-300 mb-2">
        Tactical Assessment
      </div>

      <div className="space-y-1 text-sm">
        <div>
  Detection:
  {" "}
  {Math.round(
    metrics.detection
  )}%
</div>

<div>
  Acoustic:
  {" "}
  {metrics.acousticSignature}
</div>

<div>
  Cavitation:
  {" "}
  {metrics.cavitationRisk}
</div>

        
      </div>

    </div>

  )}

</div>
        </div>

{/* METRICS */}

<div className="col-span-3 p-4 overflow-y-auto">
 

<h2 className="text-3xl font-bold mb-6">
  Performance Dashboard
</h2>

<MetricsPanel
  metrics={metrics}
/>

<div className="mt-6">

  <div className="glass-card p-5">

    <div
      className="
      text-xs
      uppercase
      tracking-widest
      text-cyan-300
      mb-4
    "
    >
      Mission Summary
    </div>

    <div className="space-y-3">

      <div>
        Estimated Range:
        {" "}
        {metrics?.estimatedRange}
        km
      </div>

      <div>
        Transit Time:
        {" "}
        {metrics?.transitTime}
        min
      </div>

      <div>
        Material:
        {" "}
        {metrics?.material}
      </div>

      <div>
        Propulsion:
        {" "}
        {metrics?.propulsion}
      </div>

    </div>

  </div>

</div>


</div>

      </div>

    </div>
  );
}
  
