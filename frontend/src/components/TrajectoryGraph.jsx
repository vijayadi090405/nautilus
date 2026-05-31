export default function TrajectoryGraph({
  speed,
  angle,
}) {

  const width = 320;
  const height = 220;

  const points = [];

  const g = 9.81;

  const velocity =
    speed * 0.514;

  const theta =
    angle * Math.PI / 180;

  let maxX = 1;
  let maxY = 1;

  for (
    let t = 0;
    t <= 20;
    t += 0.5
  ) {

    const x =
      velocity *
      Math.cos(theta) *
      t;

    const y =
      velocity *
      Math.sin(theta) *
      t -
      0.5 *
      g *
      t *
      t;

    if (y >= 0) {

      points.push({
        x,
        y
      });

      maxX =
        Math.max(
          maxX,
          x
        );

      maxY =
        Math.max(
          maxY,
          y
        );

    }

  }

  const path =
    points
      .map(
        (
          p,
          i
        ) => {

          const px =
            (
              p.x /
              maxX
            ) * width;

          const py =
            height -
            (
              p.y /
              maxY
            ) * height;

          return `${
            i === 0
              ? "M"
              : "L"
          } ${px} ${py}`;

        }
      )
      .join(" ");

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
        Tactical Prediction
      </div>

      <div
        className="
        flex
        justify-between
        items-center
        mb-4
      "
      >

        <h3
          className="
          text-xl
          font-bold
        "
        >
          Trajectory
        </h3>

        <div
          className="
          rounded-full
          bg-cyan-500/10
          px-3
          py-1
          text-xs
          text-cyan-300
        "
        >
          LIVE
        </div>

      </div>

      <svg
        width="100%"
        height="240"
        viewBox={`0 0 ${width} ${height}`}
      >

        {/* Grid */}

        {[...Array(5)].map(
          (_, i) => (

            <line
              key={i}
              x1="0"
              y1={
                i *
                (
                  height /
                  4
                )
              }
              x2={width}
              y2={
                i *
                (
                  height /
                  4
                )
              }
              stroke="rgba(255,255,255,.06)"
            />

          )
        )}

        {/* Glow */}

        <path
          d={path}
          fill="none"
          stroke="rgba(34,211,238,.25)"
          strokeWidth="10"
        />

        {/* Main Line */}

        <path
          d={path}
          fill="none"
          stroke="#22d3ee"
          strokeWidth="4"
        />

      </svg>

      <div
        className="
        mt-4
        flex
        justify-between
        text-sm
        text-slate-400
      "
      >

        <span>
          Speed:
          {" "}
          {speed}
          kn
        </span>

        <span>
          Angle:
          {" "}
          {angle}
          °
        </span>

      </div>

    </div>

  );
}