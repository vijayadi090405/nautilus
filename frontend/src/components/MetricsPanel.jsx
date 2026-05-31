export default function MetricsPanel({
  metrics,
}) {

  if (!metrics) {

    return (
      <div className="text-slate-400">
        Waiting for simulation...
      </div>
    );

  }

  const MetricCard = ({
    title,
    value,
    status
  }) => (

    <div className="
      glass-card
      p-5
      flex
      flex-col
      justify-between
      min-h-[60px]
    ">

      <div className="
        text-xs
        uppercase
        tracking-widest
        text-cyan-300
      ">
        {title}
      </div>

      <div className="
        text-2xl
        font-black
        text-white
      ">
        {value}
      </div>

      <div className="
        text-sm
        text-slate-400
      ">
        {status}
      </div>

    </div>

  );

  return (

    <div className="grid grid-cols-1 gap-4">

      <MetricCard
        title="Stability"
        value={metrics.stability}
        status="Optimal"
      />

      <MetricCard
        title="Efficiency"
        value={metrics.efficiency}
        status="Nominal"
      />

      <MetricCard
        title="Acoustic Risk"
        value={metrics.acousticRisk}
        status="Monitoring"
      />

      <MetricCard
        title="Detection Risk"
        value={metrics.detectionRisk}
        status="Tracking"
      />

      <MetricCard
        title="Mission Score"
        value={metrics.missionScore}
        status="Recommended"
      />

    </div>

  );
}