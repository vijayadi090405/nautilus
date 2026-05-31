export default function SonarPanel({
  speed,
  diameter,
  propulsion,
}) {

  const bars = [];

  for (let i = 0; i < 40; i++) {

    let value =
      Math.random() * 40;

    value += speed * 0.8;

    value += diameter * 20;

    if (
      propulsion === "Thermal"
    ) {
      value += 25;
    }

    if (
      propulsion === "Electric"
    ) {
      value -= 10;
    }

    bars.push(
      Math.max(
        5,
        Math.min(value, 100)
      )
    );
  }

  const riskLevel =
    propulsion === "Electric"
      ? "LOW"
      : propulsion === "Pump-Jet"
      ? "MEDIUM"
      : "HIGH";

  return (

    <div className="glass-card p-5">

      <div className="
        text-xs
        uppercase
        tracking-widest
        text-cyan-300
        mb-4
      ">
        Acoustic Analysis
      </div>

      <div className="
        flex
        justify-between
        items-center
        mb-4
      ">

        <h3 className="text-xl font-bold">
          Sonar Signature
        </h3>

        <div className="
          rounded-full
          px-3
          py-1
          text-xs
          bg-cyan-500/10
          text-cyan-300
        ">
          {riskLevel} RISK
        </div>

      </div>

      <div className="
        flex
        items-end
        h-52
        gap-1
      ">

        {bars.map(
          (height, index) => (

            <div
              key={index}
              className="
                flex-1
                rounded-t
                bg-cyan-400
                opacity-80
              "
              style={{
                height:
                  `${height}%`
              }}
            />

          )
        )}

      </div>

      <div className="
        mt-4
        flex
        justify-between
        text-sm
        text-slate-400
      ">

        <span>
          Propulsion:
          {" "}
          {propulsion}
        </span>

        <span>
          Speed:
          {" "}
          {speed} kn
        </span>

      </div>

    </div>

  );
}