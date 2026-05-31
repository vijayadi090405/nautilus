import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import TorpedoScene from "../components/TorpedoScene";
import SonarPanel from "../components/SonarPanel";


export default function AdvisorMode() {

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
    !recommendation
  )
    return null;

  const pros = [];
  const cons = [];

  if (
    selectedDesign.speed >=
    recommendation.speed
  ) {
    pros.push(
      "Higher speed capability"
    );
  } else {
    cons.push(
      "Lower speed than recommended design"
    );
  }

  if (
    selectedDesign.diameter <=
    recommendation.diameter
  ) {
    pros.push(
      "Smaller acoustic profile"
    );
  } else {
    cons.push(
      "Larger acoustic profile"
    );
  }

  if (
    selectedDesign.length >=
    recommendation.length
  ) {
    pros.push(
      "Improved stability"
    );
  } else {
    cons.push(
      "Reduced stability"
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

      try {

        const response =
          await axios.post(
            "http://127.0.0.1:5000/advisor",
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

setSelectedDesign(
  response.data
);

      } catch (err) {

        console.error(err);

      }

    };

  return (


    
    <div className="min-h-screen bg-slate-950 text-white">

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
                  Weight:
                  {" "}
                  {selectedDesign.weight} kg
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

<div className="mt-4">

{
recommendation.alternatives?.map(
(design,index)=>(
<div
key={index}
onClick={()=>
setSelectedDesign(design)
}
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
    Option {index + 1}
  </span>

  <span className="text-cyan-400">
    {design.score}
  </span>

</div>

</div>
))
}

</div>

<div
  onClick={() =>
    setSelectedDesign(
      recommendation.bestStealth
    )
  }
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
      Best Stealth
    </span>

    <span className="text-cyan-400">
      {
        recommendation
          .bestStealth
          ?.score
      }
    </span>

  </div>

</div>

<div
  onClick={() =>
    setSelectedDesign(
      recommendation.bestSpeed
    )
  }
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
      Best Speed
    </span>

    <span className="text-cyan-400">
      {
        recommendation
          .bestSpeed
          ?.score
      }
    </span>

  </div>

</div>

<div
  onClick={() =>
    setSelectedDesign(
      recommendation.bestRange
    )
  }
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
      Best Range
    </span>

    <span className="text-cyan-400">
      {
        recommendation
          .bestRange
          ?.score
      }
    </span>

  </div>

</div>

</div>

              <div className="mt-8">

                <SonarPanel
                  speed={
                    selectedDesign.speed
                  }
                  diameter={
                    selectedDesign.diameter
                  }
                  propulsion={
                    selectedDesign.propulsion
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