export default function MetricsPanel({
  metrics
}) {

  if (!metrics) {

    return (
      <div className="text-slate-400">
        Waiting for simulation...
      </div>
    );

  }

function getStatusColor(
  title,
  value
) {

  if (
    title === "Cavitation Risk"
  ) {

    if (value === "LOW")
      return "text-green-400";

    if (value === "MEDIUM")
      return "text-yellow-400";

    return "text-red-400";
  }

  if (
    title === "Detection Probability"
  ) {

    const v =
      Number(value);

    if (v < 20)
      return "text-green-400";

    if (v < 50)
      return "text-yellow-400";

    return "text-red-400";
  }

  if (
    title === "Acoustic Signature"
  ) {

    if (value < 0.4)
      return "text-green-400";

    if (value < 0.7)
      return "text-yellow-400";

    return "text-red-400";
  }

  return "text-white";
}

  const Card = ({
    title,
    value,
    unit
  }) => (

    <div className="glass-card p-4">

      <div
        className="
        text-xs
        uppercase
        tracking-widest
        text-cyan-300
        mb-2
      "
      >
        {title}
      </div>

      <div
  className={`
  text-2xl
  font-black
  ${getStatusColor(
      title,
      value
  )}
`}
>
        {value}
        {" "}
        {unit}
      </div>

    </div>

  );

  return (

    <div className="space-y-8">

      {/* HYDRODYNAMICS */}

      <div>

        <h3
          className="
          text-lg
          font-bold
          mb-3
        "
        >
          Hydrodynamics
        </h3>

        <div className="grid gap-3">

          <Card
            title="Drag Force"
            value={metrics.drag}
            unit="N"
          />

          <Card
            title="Power Required"
            value={metrics.powerRequired}
            unit="kW"
          />

          <Card
            title="Cavitation Risk"
            value={metrics.cavitationRisk}
            unit=""
          />

        </div>

      </div>

      {/* STRUCTURE */}

      <div>

        <h3
          className="
          text-lg
          font-bold
          mb-3
        "
        >
          Structure
        </h3>

        <div className="grid gap-3">

          <Card
            title="Hull Mass"
            value={metrics.mass}
            unit="kg"
          />

          <Card
            title="Displacement"
            value={metrics.displacement}
            unit="kg"
          />

          <Card
            title="Safety Factor"
            value={metrics.safetyFactor}
            unit=""
          />

          <Card
            title="Depth Rating"
            value={metrics.depthRating}
            unit="m"
          />

        </div>

      </div>

      {/* ENDURANCE */}

      <div>

        <h3
          className="
          text-lg
          font-bold
          mb-3
        "
        >
          Endurance
        </h3>

        <div className="grid gap-3">

          <Card
            title="Stored Energy"
            value={metrics.storedEnergy}
            unit="Wh"
          />

          <Card
            title="Endurance"
            value={metrics.endurance}
            unit="hr"
          />

          <Card
            title="Range"
            value={metrics.estimatedRange}
            unit="km"
          />

        </div>

      </div>

      {/* SIGNATURES */}

      <div>

        <h3
          className="
          text-lg
          font-bold
          mb-3
        "
        >
          Signatures
        </h3>

        <div className="grid gap-3">

          <Card
            title="Source Level"
            value={metrics.sourceLevel}
            unit="dB"
          />

          <Card
            title="Detection Probability"
            value={metrics.detection}
            unit="%"
          />
<Card
  title="Target Strength"
  value={metrics.targetStrength}
  unit="dB"
/>

<Card
  title="Ambient Noise"
  value={metrics.ambientNoise}
  unit="dB"
/>

<Card
  title="Directivity Index"
  value={metrics.directivityIndex}
  unit="dB"
/>

<Card
  title="Detection Threshold"
  value={metrics.detectionThreshold}
  unit="dB"
/>
          <Card
            title="Acoustic Index"
            value={metrics.acousticSignature}
            unit=""
          />

          <Card
            title="Magnetic Index"
            value={metrics.magneticSignature}
            unit=""
          />

          <Card
            title="Thermal Index"
            value={metrics.thermalSignature}
            unit=""
          />

        </div>

      </div>
      <div>

        <h3
          className="
          text-lg
          font-bold
          mb-3
          "
        >
          Engineering Assessment
        </h3>

        <div className="glass-card p-4">

          <ul className="space-y-3">

            {metrics.recommendations?.map(

              (item, index) => (

                <li
                  key={index}
                  className="
                  text-sm
                  text-slate-300
                  "
                >

                  • {item}

                </li>

              )

            )}

          </ul>

        </div>

      </div>
    </div>

  );

}