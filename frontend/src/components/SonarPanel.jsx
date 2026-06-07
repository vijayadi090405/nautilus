export default function SonarPanel({
  sourceLevel = 0,
  detection = 0,
  propulsion = "Unknown",
  coating = "Unknown",
  acousticSignature = 0,
  magneticSignature = 0,
  thermalSignature = 0
}){

let noiseClass;

if (acousticSignature < 0.3) {

  noiseClass = "Very Quiet";

}
else if (acousticSignature < 0.6) {

  noiseClass = "Low";

}
else if (acousticSignature < 0.8) {

  noiseClass = "Moderate";

}
else {

  noiseClass = "High";

}
let riskLevel;

if (detection < 5) {

  riskLevel = "LOW";

}
else if (detection < 20) {

  riskLevel = "MEDIUM";

}
else {

  riskLevel = "HIGH";

}
  return (

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
        Acoustic Assessment
      </div>

      <h3 className="text-xl font-bold mb-5">
        Sonar & Signature Analysis
      </h3>

      <div className="space-y-4">

        <div>

          Source Level:

          {" "}

          {sourceLevel.toFixed(1)}

          {" "}dB

        </div>

        <div>

          Detection Probability:

          {" "}

          {detection.toFixed(1)}

          {" "}%

        </div>

        <div>

          Risk Level:

          {" "}

          {riskLevel}

        </div>

        <div>

          Coating:

          {" "}

          {coating}

        </div>

        <div>

          Noise Class:

          {" "}

          {noiseClass}

        </div>
<div>

  Acoustic Signature:

  {" "}

  {acousticSignature?.toFixed(2)}

</div>

<div>

  Magnetic Signature:

  {" "}

  {magneticSignature?.toFixed(2)}

</div>

<div>

  Thermal Signature:

  {" "}

  {thermalSignature?.toFixed(2)}

</div>
      </div>

    </div>

  );
}