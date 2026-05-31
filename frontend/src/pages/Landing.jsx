import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import {
  Radar,
  Brain,
  BarChart3,
  Target
} from "lucide-react";

export default function Landing() {

  const navigate = useNavigate();

  const cards = [
    {
      title: "Design & Simulate",
      description:
        "Create custom underwater vehicle configurations and analyze trajectory, sonar signature and performance.",
      route: "/design",
      icon: <Radar size={48} />
    },

    {
      title: "AI Advisor",
      description:
        "Generate AI-assisted recommendations based on mission requirements.",
      route: "/advisor",
      icon: <Brain size={48} />
    },



  ];

  return (

    <div className="relative min-h-screen overflow-hidden text-white">
<div className="radar-ring ring1" />
<div className="radar-ring ring2" />
<div className="radar-ring ring3" />
<div className="sonar-sweep" />

{[...Array(25)].map((_, i) => (
  <div
    key={i}
    className="particle"
  />
))}
      {/* Glow 1 */}
      <div className="absolute left-0 top-0 h-[600px] w-[600px] rounded-full bg-cyan-500/10 blur-[150px]" />

      {/* Glow 2 */}
      <div className="absolute right-0 bottom-0 h-[500px] w-[500px] rounded-full bg-blue-500/10 blur-[150px]" />

      <div className="relative z-10 mx-auto max-w-7xl px-8 py-16">

        <div className="mb-20 text-center">

          <div className="mb-4 inline-block rounded-full border border-cyan-400/20 bg-cyan-400/10 px-4 py-2 text-sm text-cyan-300">
            AI-Assisted Naval Design Platform
          </div>

          <h1 className="text-white text-6xl font-black tracking-tight md:text-8xl">
            NAUTILUS
          </h1>

          <p className="mt-6 max-w-4xl text-xl text-slate-400">
            Underwater Vehicle Design, Optimization,
            Mission Analysis and Decision Support Platform.
          </p>

        </div>

        <div className="grid gap-8 mt-16 md:grid-cols-2">

          {cards.map((card) => (

            <motion.div
              key={card.title}
              whileHover={{
                scale: 1.02,
                y: -6
              }}
              transition={{
                duration: 0.2
              }}
              onClick={() =>
                navigate(card.route)
              }
              className="
                glass-card
                cursor-pointer
                p-8
                min-h-[260px]
                flex
                flex-col
                justify-between
              "
            >

              <div>

                <div className="mb-6 text-cyan-300">
                  {card.icon}
                </div>

                <h2 className="mb-4 text-3xl font-bold text-white">
                  {card.title}
                </h2>

                <p className="leading-relaxed text-slate-400">
                  {card.description}
                </p>

              </div>

              <div className="mt-8 font-semibold text-cyan-300">
                Open Module →
              </div>

            </motion.div>

          ))}

        </div>

      </div>

    </div>
  );
}