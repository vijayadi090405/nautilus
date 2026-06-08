import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import TorpedoScene from "../components/TorpedoScene";
import SonarPanel from "../components/SonarPanel";


export default function AdvisorMode() {
const [loading, setLoading] =
  useState(false);
  const navigate = useNavigate();
const [selectedDesign,
  setSelectedDesign] =
  useState(null);
  const [missionType, setMissionType] =
    useState("Anti-Submarine");

  const [range, setRange] =
    useState(50);

  const [stealth, setStealth] =
    useState("High");

  const [depth, setDepth] =
    useState("Deep");

  const [recommendation,
    setRecommendation] =
    useState(null);

    const [panelWidth,
  setPanelWidth] =
  useState(350);

const getTradeoff = () => {

  if (
    !selectedDesign ||
    !recommendation ||
    selectedDesign === recommendation
  ) {
    return {
      pros: [
        "Reference design selected"
      ],
      cons: []
    };
  }

  const pros = [];
  const cons = [];

  if (
    selectedDesign.speed >
    recommendation.speed
  ) {
    pros.push(
      "Higher speed capability"
    );
  } else {
    cons.push(
      "Lower speed capability"
    );
  }

  if (
    selectedDesign.detection <
    recommendation.detection
  ) {
    pros.push(
      "Lower detection probability"
    );
  } else {
    cons.push(
      "Higher detection probability"
    );
  }

  if (
    selectedDesign.survivability >
    recommendation.survivability
  ) {
    pros.push(
      "Higher survivability"
    );
  } else {
    cons.push(
      "Lower survivability"
    );
  }

  if (
    selectedDesign.estimatedRange >
    recommendation.estimatedRange
  ) {
    pros.push(
      "Greater operational range"
    );
  } else {
    cons.push(
      "Reduced operational range"
    );
  }

  return {
    pros,
    cons
  };
};

const tradeoff =
  getTradeoff();
  const generateRecommendation =
    async () => {
      console.log("GENERATE CLICKED");

console.log({
  missionType,
  range,
  stealth,
  depth
});

      try {
setLoading(true);
        const response =
          await axios.post(
            "https://nautilus-lsmu.onrender.com/advisor",
            {
              missionType,
              range,
              stealth,
              depth,
            }
          );

setRecommendation(
  response.data
);
console.log(
  response.data.missionSimulation
);
setSelectedDesign(
  response.data
);
setLoading(false);

      } catch (err) {

  console.error(err);

  setLoading(false);

}

    };

  return (


    
    <div className="min-h-screen bg-slate-950 text-white">
{loading && (
  <div
    className="
    fixed
    inset-0
    z-50
    bg-black/80
    flex
    flex-col
    items-center
    justify-center
    "
  >

    <div
      className="
      animate-spin
      rounded-full
      h-20
      w-20
      border-b-4
      border-cyan-400
      "
    />

    <div className="mt-6 text-xl">

Running Analysis...

    </div>

  </div>
)}
      <div className="ai-glow" />

<div className="hex-grid" />

<div className="neural-network" />
<div className="advisor-core" />

      <div className="relative z-10 flex h-screen overflow-hidden">

        {/* INPUTS */}

        <div
  className="
    p-4
    overflow-y-auto
    h-screen
  "
  style={{
    width: "420px"
  }}
>

  <div className="glass-card p-6 h-full">
<button
  onClick={() => navigate("/")}
  className="glass-button px-4 py-2 mb-6"
>
  ← Back
</button>

          <h1 className="text-3xl font-bold mb-8">
            AI Advisor
          </h1>

          <div className="mb-6">

            <label>
              Mission Type
            </label>

            <select
              className="w-full p-2 mt-2 bg-slate-800 rounded"
              value={missionType}
              onChange={(e)=>
                setMissionType(
                  e.target.value
                )
              }
            >
              <option>
                Anti-Submarine
              </option>

              <option>
                Coastal Defense
              </option>

              <option>
                Deep Strike
              </option>

            </select>

          </div>

          <div className="mb-6">

            <label>
              Range
            </label>

            <div className="flex gap-3 items-center">

<input
  type="range"
  min="10"
  max="100"
  value={range}
  onChange={(e) =>
    setRange(
      Number(e.target.value)
    )
  }
  style={{
    width: "100%"
  }}
/>

  <input
    type="number"
    value={range}
    onChange={(e)=>
      setRange(
        Number(
          e.target.value
        )
      )
    }
    className="
      w-20
      bg-slate-800
      rounded
      p-2
      text-center
    "
  />

</div>

          </div>

          <div className="mb-6">

            <label>
              Stealth
            </label>

            <select
              className="w-full p-2 mt-2 bg-slate-800 rounded"
              value={stealth}
              onChange={(e)=>
                setStealth(
                  e.target.value
                )
              }
            >
              <option>
                High
              </option>

              <option>
                Medium
              </option>

              <option>
                Low
              </option>

            </select>

          </div>

          <div className="mb-6">

            <label>
              Depth
            </label>

            <select
              className="w-full p-2 mt-2 bg-slate-800 rounded"
              value={depth}
              onChange={(e)=>
                setDepth(
                  e.target.value
                )
              }
            >
              <option>
                Shallow
              </option>

              <option>
                Deep
              </option>

            </select>

          </div>

          <button
            onClick={
              generateRecommendation
            }
            className="w-full bg-cyan-500 text-black font-bold p-3 rounded-xl "
          >
            Generate Recommendation
</button>

  </div>

</div>

        {/* MODEL */}

        <div className="flex-1">

          {recommendation && (

            <TorpedoScene
              diameter={
                selectedDesign?.diameter
              }
              length={
                selectedDesign?.length
              }
              propulsion={
                selectedDesign?.propulsion
              }
            />

          )}

        </div>

        {/* OUTPUT */}



<div
  className="
    col-span-3 
    p-4
    overflow-y-auto
    h-screen
  "
  style={{
    width: "300px"
  }}
>


        

          <h2 className="text-2xl font-bold mb-4">
            Recommendation
          </h2>

          {recommendation && (

            <>

              <div className="space-y-3">

                <div>
                  Diameter:
                  {" "}
                  {selectedDesign.diameter} m
                </div>

                <div>
                  Length:
                  {" "}
                  {selectedDesign.length} m
                </div>

                <div>
                  Mass:
                  {" "}
                  {selectedDesign.mass} kg
                </div>

                <div>
                  Speed:
                  {" "}
                  {selectedDesign.speed} knots
                </div>

                <div>
                  Propulsion:
                  {" "}
                  {selectedDesign.propulsion}
                </div>
                <div>

  Hull Material:

  {" "}

  {selectedDesign?.material}

</div>

<div>

  Hull Coating:

  {" "}

  {selectedDesign?.coating}

</div>

<div>

  Design Philosophy:

  {" "}

  {selectedDesign?.designType}

</div>

<div>
  Detection Probability:
  {" "}
  {selectedDesign?.detection} %
</div>

<div>
  Source Level:
  {" "}
  {selectedDesign?.sourceLevel}
  {" "}dB
</div>

<div>
  Drag Force:
  {" "}
  {selectedDesign?.drag}
  {" "}N
</div>

<div>
  Safety Factor:
  {" "}
  {selectedDesign?.safetyFactor}
</div>

<div>
  Survivability:
  {" "}
  {selectedDesign?.survivability}
</div>
<div
  className="
  mt-4
  p-3
  rounded-xl
  bg-cyan-900/30
  border border-cyan-500/30
  "
>
  Advisor Confidence:
  {" "}
  {selectedDesign?.confidence}%
</div>
{
recommendation?.missionSimulation && (

<div
className="
mt-4
bg-slate-900
rounded-xl
p-4
border
border-cyan-500/30
"
>

<h3
className="
text-cyan-400
font-bold
mb-2
"
>
Mission Simulation
</h3>

<div>
Mission Success:
{" "}
{
recommendation
?.missionSimulation
?.missionSuccess
}
%
</div>

<div>
Escape Probability:
{" "}
{
recommendation
?.missionSimulation
?.escapeProbability
}
%
</div>

<div>
Target Detected:
{" "}
{
recommendation
?.missionSimulation
?.targetDetected
? "YES"
: "NO"
}
</div>

<div>
Attack Success:
{" "}
{
recommendation
?.missionSimulation
?.attackSuccess
? "YES"
: "NO"
}
</div>

<div className="mt-4">

<h4 className="font-bold">
Mission Timeline
</h4>

{
recommendation
?.missionSimulation
?.timeline
?.map(
(step,index)=>(
<div
key={index}
className="mt-2"
>
✓ {step.phase}
</div>
)
)
}

</div>

</div>

)
}

{
recommendation?.riskAnalysis && (

<div
className="
mt-4
bg-slate-900
rounded-xl
p-4
border
border-yellow-500/30
"
>

<h3
className="
text-yellow-400
font-bold
mb-4
"
>
Monte Carlo Risk Analysis
</h3>

<div className="grid grid-cols-2 gap-3">

<div className="glass-card p-3">
<div className="text-xs text-cyan-300">
Mean Success
</div>
<div className="text-xl font-bold">
{
recommendation.riskAnalysis
.meanMissionSuccess
}%
</div>
</div>

<div className="glass-card p-3">
<div className="text-xs text-cyan-300">
Success Rate
</div>
<div className="text-xl font-bold">
{
recommendation.riskAnalysis
.successRate
}%
</div>
</div>

<div className="glass-card p-3">
<div className="text-xs text-cyan-300">
P10
</div>
<div className="text-xl font-bold">
{
recommendation.riskAnalysis
.p10MissionSuccess
}%
</div>
</div>

<div className="glass-card p-3">
<div className="text-xs text-cyan-300">
P90
</div>
<div className="text-xl font-bold">
{
recommendation.riskAnalysis
.p90MissionSuccess
}%
</div>
</div>

<div className="glass-card p-3">
<div className="text-xs text-cyan-300">
Std Dev
</div>
<div className="text-xl font-bold">
{
recommendation.riskAnalysis
.stdMissionSuccess
}
</div>
</div>

<div className="glass-card p-3">
<div className="text-xs text-cyan-300">
Risk Level
</div>

<div
className={`
text-xl
font-bold
${
recommendation.riskAnalysis
.riskLevel === "LOW"
? "text-green-400"
: recommendation.riskAnalysis
.riskLevel === "MEDIUM"
? "text-yellow-400"
: "text-red-400"
}
`}
>
{
recommendation.riskAnalysis
.riskLevel
}
</div>

</div>

</div>

</div>

)
}

<div className="mt-6">

  <h3 className="text-xl font-bold">
    Why This Design Was Chosen
  </h3>

  <div className="glass-card p-4 mt-3">

    {
(selectedDesign?.reasoning || []).map(
        (item, index) => (
          <div key={index}>
            ✓ {item}
          </div>
        )
      )
    }

  </div>

</div>
<div className="mt-6">

  <h3 className="text-xl font-bold">
    AI Tradeoffs
  </h3>

  <div className="glass-card p-4 mt-3">

    {
(selectedDesign?.tradeoffs || []).map(
        (item, index) => (
          <div key={index}>
            ⚠ {item}
          </div>
        )
      )
    }

  </div>

</div>
</div>

<div className="mt-8">

<h3 className="
mt-8
text-xl
font-bold
">
Tradeoff Analysis
</h3>

<div className="glass-card p-4 mt-3">

  <div className="text-green-400 mb-2">
    Advantages
  </div>

  {
    tradeoff?.pros.map(
      (item,index)=>(
        <div key={index}>
          ✓ {item}
        </div>
      )
    )
  }

  <div className="
  text-red-400
  mt-4
  mb-2
  ">
    Disadvantages
  </div>

  {
    tradeoff?.cons.map(
      (item,index)=>(
        <div key={index}>
          ✗ {item}
        </div>
      )
    )
  }

</div>

<h3 className="
mt-8
text-xl
font-bold
">
Alternative Designs
</h3>
<div
  onClick={() =>
    setSelectedDesign(
      recommendation
    )
  }
  className="
  mt-3
  cursor-pointer
  rounded-xl
  bg-green-900/30
  border border-green-500/30
  p-3
  "
>

  <div className="flex justify-between">

    <span>
      ⭐ Recommended
    </span>

    <span className="text-green-400">
      {recommendation.score}
    </span>

  </div>

</div>
<div className="mt-4">

{
recommendation.alternatives?.map(
(design,index)=>(
<div
key={index}
onClick={() => {

  console.log(design);

  setSelectedDesign(design);

}}
className="
mt-3
cursor-pointer
rounded-xl
bg-slate-900
p-3
"
>

<div className="flex justify-between">

  <span>
    Alternative {index + 1}
  </span>

  <span className="text-cyan-400">
    {design.score}
  </span>

</div>

</div>
))
}

</div>


</div>

<div className="mt-8">

<SonarPanel
  sourceLevel={
    selectedDesign?.sourceLevel || 0
  }

  detection={
    selectedDesign?.detection || 0
  }

  propulsion={
    selectedDesign?.propulsion
  }

  coating={
    selectedDesign?.coating
  }

  acousticSignature={
    selectedDesign?.acousticSignature
  }

  magneticSignature={
    selectedDesign?.magneticSignature
  }

  thermalSignature={
    selectedDesign?.thermalSignature
  }
/>

              </div>

            </>

          )}

        </div>

  </div>

</div>

   

  );
}
