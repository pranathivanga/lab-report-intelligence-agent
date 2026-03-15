"use client";
import { useState, useRef } from "react";

// ─── Icons (inline SVG components) ───────────────────────────────────────────
const UploadIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="w-10 h-10">
    <path strokeLinecap="round" strokeLinejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
  </svg>
);

const HeartPulseIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="w-5 h-5">
    <path strokeLinecap="round" strokeLinejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
  </svg>
);

const ShieldIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="w-5 h-5">
    <path strokeLinecap="round" strokeLinejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.955 11.955 0 003 10c0 5.592 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.57-.598-3.75h-.152c-3.196 0-6.1-1.249-8.25-3.286z" />
  </svg>
);

const CheckIcon = () => (
  <svg viewBox="0 0 24 24" fill="currentColor" className="w-4 h-4">
    <path fillRule="evenodd" d="M2.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12zm13.36-1.814a.75.75 0 10-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 00-1.06 1.06l2.25 2.25a.75.75 0 001.14-.094l3.75-5.25z" clipRule="evenodd" />
  </svg>
);

const AlertIcon = () => (
  <svg viewBox="0 0 24 24" fill="currentColor" className="w-4 h-4">
    <path fillRule="evenodd" d="M9.401 3.003c1.155-2 4.043-2 5.197 0l7.355 12.748c1.154 1.998-.29 4.5-2.599 4.5H4.645c-2.309 0-3.752-2.502-2.598-4.5L9.4 3.003zM12 8.25a.75.75 0 01.75.75v3.75a.75.75 0 01-1.5 0V9a.75.75 0 01.75-.75zm0 8.25a.75.75 0 100-1.5.75.75 0 000 1.5z" clipRule="evenodd" />
  </svg>
);

const InfoIcon = () => (
  <svg viewBox="0 0 24 24" fill="currentColor" className="w-4 h-4">
    <path fillRule="evenodd" d="M2.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12zm8.706-1.442c1.146-.573 2.437.463 2.126 1.706l-.709 2.836.042-.02a.75.75 0 01.67 1.34l-.04.022c-1.147.573-2.438-.463-2.127-1.706l.71-2.836-.042.02a.75.75 0 11-.671-1.34l.041-.022zM12 9a.75.75 0 100-1.5.75.75 0 000 1.5z" clipRule="evenodd" />
  </svg>
);

const DoctorIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="w-6 h-6">
    <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
  </svg>
);

const SparkleIcon = () => (
  <svg viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
    <path fillRule="evenodd" d="M9 4.5a.75.75 0 01.721.544l.813 2.846a3.75 3.75 0 002.576 2.576l2.846.813a.75.75 0 010 1.442l-2.846.813a3.75 3.75 0 00-2.576 2.576l-.813 2.846a.75.75 0 01-1.442 0l-.813-2.846a3.75 3.75 0 00-2.576-2.576l-2.846-.813a.75.75 0 010-1.442l2.846-.813A3.75 3.75 0 007.466 7.89l.813-2.846A.75.75 0 019 4.5zM18 1.5a.75.75 0 01.728.568l.258 1.036c.236.94.97 1.674 1.91 1.91l1.036.258a.75.75 0 010 1.456l-1.036.258c-.94.236-1.674.97-1.91 1.91l-.258 1.036a.75.75 0 01-1.456 0l-.258-1.036a2.625 2.625 0 00-1.91-1.91l-1.036-.258a.75.75 0 010-1.456l1.036-.258a2.625 2.625 0 001.91-1.91l.258-1.036A.75.75 0 0118 1.5z" clipRule="evenodd" />
  </svg>
);

// ─── Circular Gauge ───────────────────────────────────────────────────────────
function CircularGauge({ score }) {
  const r = 70;
  const cx = 90;
  const cy = 90;
  const circumference = Math.PI * r; // half circle
  const dash = score != null ? (score / 100) * circumference : 0;

  const color =
    score == null ? "#CBD5E1"
    : score <= 35 ? "#34D399"
    : score <= 65 ? "#FBBF24"
    : "#F87171";

  const label =
    score == null ? "—"
    : score <= 35 ? "Low Risk"
    : score <= 65 ? "Moderate"
    : "High Risk";

  const labelColor =
    score == null ? "#94A3B8"
    : score <= 35 ? "#059669"
    : score <= 65 ? "#D97706"
    : "#DC2626";

  return (
    <div className="flex flex-col items-center gap-2">
      <svg width="180" height="100" viewBox="0 0 180 100">
        {/* background arc */}
        <path
          d={`M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`}
          fill="none"
          stroke="#E2E8F0"
          strokeWidth="12"
          strokeLinecap="round"
        />
        {/* colored arc */}
        {score != null && (
          <path
            d={`M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`}
            fill="none"
            stroke={color}
            strokeWidth="12"
            strokeLinecap="round"
            strokeDasharray={`${dash} ${circumference}`}
            style={{ transition: "stroke-dasharray 1s ease" }}
          />
        )}
        {/* score text */}
        <text x={cx} y={cy - 14} textAnchor="middle" fontSize="32" fontWeight="700" fill="#1E293B" fontFamily="'DM Serif Display', serif">
          {score ?? "—"}
        </text>
        <text x={cx} y={cy + 4} textAnchor="middle" fontSize="11" fill="#94A3B8" fontFamily="'DM Sans', sans-serif" letterSpacing="1">
          out of 100
        </text>
      </svg>
      <span className="text-sm font-semibold tracking-wide px-4 py-1 rounded-full" style={{ color: labelColor, backgroundColor: labelColor + "18" }}>
        {label}
      </span>
    </div>
  );
}

// ─── Status Badge ─────────────────────────────────────────────────────────────
function StatusBadge({ status }) {
  const styles = {
    Normal: { bg: "bg-emerald-50", text: "text-emerald-700", border: "border-emerald-200", icon: <CheckIcon /> },
    Low:    { bg: "bg-blue-50",    text: "text-blue-700",    border: "border-blue-200",    icon: <AlertIcon /> },
    High:   { bg: "bg-rose-50",    text: "text-rose-700",    border: "border-rose-200",    icon: <AlertIcon /> },
  };
  const s = styles[status] || styles.Normal;
  return (
    <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold border ${s.bg} ${s.text} ${s.border}`}>
      {s.icon}
      {status}
    </span>
  );
}

// ─── Confidence Meter [NEW] ───────────────────────────────────────────────────
// Displays interpretation clarity as a horizontal progress bar.
// `confidence` is 0.0–1.0 from the API; we render it as a percentage.
function ConfidenceMeter({ confidence }) {
  const pct = Math.round(confidence * 100);
  // Color shifts from amber (low clarity) to teal (high clarity)
  const barColor =
    pct >= 75 ? "bg-teal-400"
    : pct >= 45 ? "bg-amber-400"
    : "bg-slate-300";

  return (
    <div className="mt-2">
      <div className="flex items-center justify-between mb-1">
        <span className="text-xs text-slate-400">Interpretation clarity</span>
        <span className="text-xs font-semibold text-slate-500">{pct}%</span>
      </div>
      <div className="h-1.5 w-full bg-slate-100 rounded-full overflow-hidden">
        <div
          className={`h-full rounded-full transition-all duration-700 ${barColor}`}
          style={{ width: `${pct}%` }}
        />
      </div>
      <p className="text-xs text-slate-400 mt-1 italic">not diagnostic certainty</p>
    </div>
  );
}

// ─── Lab Value Row [MODIFIED — added confidence prop + ConfidenceMeter] ───────
function LabValueRow({ test, value, normalRange, status, confidence, isLast }) {
  const isAbnormal = status !== "Normal";
  return (
    <div className={`py-4 ${!isLast ? "border-b border-slate-100" : ""} ${isAbnormal ? "bg-rose-50/30 -mx-4 px-4 rounded-xl" : ""}`}>
      {/* — existing top row — unchanged layout */}
      <div className="flex items-center gap-4">
        <div className="flex-1 min-w-0">
          <p className={`text-sm font-semibold ${isAbnormal ? "text-slate-800" : "text-slate-700"}`}>{test}</p>
          <p className="text-xs text-slate-400 mt-0.5">Normal: {normalRange}</p>
        </div>
        <div className="text-right mr-4">
          <p className={`text-base font-bold ${isAbnormal ? "text-rose-600" : "text-slate-800"}`}>{value}</p>
        </div>
        <div className="flex-shrink-0">
          <StatusBadge status={status} />
        </div>
      </div>
      {/* — NEW: confidence meter, only rendered when value is present — */}
      {confidence != null && <ConfidenceMeter confidence={confidence} />}
    </div>
  );
}

// ─── Upload Zone ──────────────────────────────────────────────────────────────
function UploadZone({ onUpload }) {
  const inputRef = useRef(null);
  const [dragging, setDragging] = useState(false);
  const [fileName, setFileName] = useState(null);

  const handleFile = (file) => {
    if (!file) return;
    setFileName(file.name);
    onUpload?.(file);
  };

  return (
    <div
      onClick={() => inputRef.current?.click()}
      onDragOver={(e) => { e.preventDefault(); setDragging(true); }}
      onDragLeave={() => setDragging(false)}
      onDrop={(e) => { e.preventDefault(); setDragging(false); handleFile(e.dataTransfer.files[0]); }}
      className={`relative cursor-pointer rounded-2xl border-2 border-dashed transition-all duration-300 p-10 flex flex-col items-center gap-4 text-center
        ${dragging ? "border-teal-400 bg-teal-50" : fileName ? "border-teal-300 bg-teal-50/50" : "border-slate-200 bg-slate-50 hover:border-teal-300 hover:bg-teal-50/30"}`}
    >
      <input
        ref={inputRef}
        type="file"
        accept=".pdf,.txt"
        className="hidden"
        onChange={(e) => handleFile(e.target.files?.[0])}
      />
      <div className={`p-4 rounded-2xl transition-colors duration-300 ${fileName ? "bg-teal-100 text-teal-600" : "bg-white text-slate-400 shadow-sm"}`}>
        <UploadIcon />
      </div>
      {fileName ? (
        <>
          <p className="text-base font-semibold text-teal-700">{fileName}</p>
          <p className="text-sm text-slate-500">File ready to analyze • Click to change</p>
        </>
      ) : (
        <>
          <div>
            <p className="text-base font-semibold text-slate-700">Drop your lab report here</p>
            <p className="text-sm text-slate-400 mt-1">or click to browse your files</p>
          </div>
          <p className="text-xs text-slate-400 bg-white px-3 py-1.5 rounded-full border border-slate-200">
            Supports PDF and TXT files
          </p>
        </>
      )}
    </div>
  );
}

// ─── Section Wrapper ──────────────────────────────────────────────────────────
function Section({ children, className = "" }) {
  return (
    <div className={`bg-white rounded-3xl shadow-sm border border-slate-100 p-6 md:p-8 ${className}`}>
      {children}
    </div>
  );
}

function SectionTitle({ children, subtitle }) {
  return (
    <div className="mb-6">
      <h2 className="text-lg font-bold text-slate-800" style={{ fontFamily: "'DM Serif Display', serif" }}>{children}</h2>
      {subtitle && <p className="text-sm text-slate-400 mt-1">{subtitle}</p>}
    </div>
  );
}

// ─── Main Dashboard ───────────────────────────────────────────────────────────
export default function LabReportDashboard() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  // Simulated analysis trigger — replace with real API call
 const handleAnalyze = async () => {
  if (!file) return;
  setLoading(true);

  try {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    console.log("API RESPONSE:", data);

    setResult({
      riskScore: data.risk_score,          // 🔥 FIXED
      summary: data.summary,
      labValues: data.labValues,
      explanation: data.explanation,
      questions: data.questions,
    });

  } catch (err) {
    console.error("Analysis error:", err);
    alert("We could not analyze this report. Please try a different file.");
  } finally {
    setLoading(false);
  }
};

  return (
    <>
      {/* Google Fonts */}
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600;700&display=swap');
        * { font-family: 'DM Sans', sans-serif; }
      `}</style>

      <div className="min-h-screen" style={{ background: "linear-gradient(135deg, #F0FDFA 0%, #F8FAFC 50%, #EFF6FF 100%)" }}>

        {/* ── Header ── */}
        <header className="sticky top-0 z-20 bg-white/80 backdrop-blur-md border-b border-slate-100">
          <div className="max-w-5xl mx-auto px-6 py-4 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-teal-500 to-cyan-600 flex items-center justify-center shadow-sm">
                <HeartPulseIcon />
                <span className="sr-only">Logo</span>
              </div>
              <div>
                <h1 className="text-base font-bold text-slate-800 leading-tight" style={{ fontFamily: "'DM Serif Display', serif" }}>
                  Lab Report Intelligence
                </h1>
                <p className="text-xs text-slate-400 leading-tight">Understand your results, simply</p>
              </div>
            </div>
            <div className="hidden sm:flex items-center gap-1.5 text-xs text-slate-500 bg-slate-50 px-3 py-1.5 rounded-full border border-slate-200">
              <ShieldIcon />
              <span>Private & Secure</span>
            </div>
          </div>
        </header>

        <main className="max-w-5xl mx-auto px-6 py-10 space-y-6">

          {/* ── Hero tagline ── */}
          <div className="text-center py-4">
            <h2 className="text-3xl md:text-4xl font-bold text-slate-800 leading-tight" style={{ fontFamily: "'DM Serif Display', serif" }}>
              Understand your lab reports<br className="hidden md:block" />{" "}
              <span className="text-transparent bg-clip-text" style={{ backgroundImage: "linear-gradient(90deg, #0D9488, #0284C7)" }}>
                in simple language
              </span>
            </h2>
            <p className="text-slate-500 mt-3 text-base max-w-xl mx-auto">
              Upload your report and our AI will explain your results clearly — no medical degree needed.
            </p>
          </div>

          {/* ── Upload Card ── */}
          <Section>
            <SectionTitle subtitle="Your file is processed securely and never stored.">
              Upload Your Lab Report
            </SectionTitle>
            <UploadZone onUpload={(f) => { setFile(f); setResult(null); }} />
            <button
              onClick={handleAnalyze}
              disabled={!file || loading}
              className={`mt-5 w-full py-3.5 rounded-2xl font-semibold text-base transition-all duration-300 flex items-center justify-center gap-2
                ${file && !loading
                  ? "bg-gradient-to-r from-teal-500 to-cyan-600 text-white shadow-md hover:shadow-lg hover:scale-[1.01] active:scale-100"
                  : "bg-slate-100 text-slate-400 cursor-not-allowed"}`}
            >
              {loading ? (
                <>
                  <svg className="animate-spin w-4 h-4" viewBox="0 0 24 24" fill="none">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
                  </svg>
                  Analyzing your report…
                </>
              ) : (
                <>
                  <SparkleIcon />
                  Analyze My Report
                </>
              )}
            </button>
          </Section>

          {/* ── Results — shown after analysis ── */}
          {result && (
            <>
              {/* ── Risk Score ── */}
              <div className="grid md:grid-cols-2 gap-6">
                <Section className="flex flex-col items-center justify-center text-center">
                  <SectionTitle subtitle="Based on your lab values">Overall Risk Score</SectionTitle>
                  <CircularGauge score={result.riskScore} />
                  {result.riskScore == null && (
                    <p className="text-sm text-slate-400 mt-4 max-w-xs">
                      Connect to the API to populate your risk score automatically.
                    </p>
                  )}
                </Section>

                {/* ── At a Glance [MODIFIED — now reads from result.summary] ── */}
          <Section className="flex flex-col justify-between">
  <SectionTitle subtitle="Summary of flagged values">At a Glance</SectionTitle>

  <div className="grid grid-cols-2 gap-4 flex-1">
    {(() => {
      const glanceStyles = {
        teal: {
          card: "bg-teal-50 border border-teal-100",
          text: "text-teal-600",
        },
        emerald: {
          card: "bg-emerald-50 border border-emerald-100",
          text: "text-emerald-600",
        },
        blue: {
          card: "bg-blue-50 border border-blue-100",
          text: "text-blue-600",
        },
        rose: {
          card: "bg-rose-50 border border-rose-100",
          text: "text-rose-600",
        },
      };

      const items = [
        { label: "Tests Analyzed", color: "teal", value: result.summary?.tests_analyzed },
        { label: "Normal Values", color: "emerald", value: result.summary?.normal_count },
        { label: "Values Low", color: "blue", value: result.summary?.low_count },
        { label: "Values High", color: "rose", value: result.summary?.high_count },
      ];

      return items.map(({ label, color, value }) => (
        <div
          key={label}
          className={`rounded-2xl p-4 flex flex-col gap-1 ${glanceStyles[color].card}`}
        >
          <span
            className="text-2xl font-bold text-slate-800"
            style={{ fontFamily: "'DM Serif Display', serif" }}
          >
            {value ?? "—"}
          </span>
          <span className={`text-xs font-medium ${glanceStyles[color].text}`}>
            {label}
          </span>
        </div>
      ));
    })()}
  </div>
</Section>
              </div>

              {/* ── Lab Values Table ── */}
              <Section>
                <SectionTitle subtitle="Each test compared to the healthy reference range">Your Lab Values</SectionTitle>

                {result.labValues.length === 0 ? (
                  <div className="text-center py-10 text-slate-400">
                    <div className="w-14 h-14 bg-slate-100 rounded-2xl flex items-center justify-center mx-auto mb-3">
                      <InfoIcon />
                    </div>
                    <p className="text-sm font-medium">Lab values will appear here after analysis</p>
                    <p className="text-xs mt-1">Connect the API to populate this section</p>
                  </div>
                ) : (
                  <div>
                    {/* Table header */}
                    <div className="flex items-center gap-4 pb-3 border-b border-slate-100 px-0">
                      <div className="flex-1 text-xs font-semibold text-slate-400 uppercase tracking-wider">Test Name</div>
                      <div className="text-xs font-semibold text-slate-400 uppercase tracking-wider mr-4">Your Value</div>
                      <div className="text-xs font-semibold text-slate-400 uppercase tracking-wider w-20 flex-shrink-0">Status</div>
                    </div>
                    {result.labValues.map((row, i) => (
                      <LabValueRow key={i} {...row} isLast={i === result.labValues.length - 1} />
                    ))}
                  </div>
                )}
              </Section>

              {/* ── Explanation ── */}
              <Section style={{ background: "linear-gradient(135deg, #F0FDFA 0%, #EFF6FF 100%)" }}>
                <div className="flex items-start gap-3 mb-5">
                  <div className="w-9 h-9 rounded-xl bg-teal-100 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <SparkleIcon />
                  </div>
                  <div>
                    <h2 className="text-lg font-bold text-slate-800" style={{ fontFamily: "'DM Serif Display', serif" }}>
                      What does this mean?
                    </h2>
                    <p className="text-sm text-slate-500 mt-0.5">Written in plain English, just for you</p>
                  </div>
                </div>

                <div className="prose prose-sm max-w-none">
                  {result.explanation ? (
                    <p className="text-slate-700 leading-relaxed text-base">{result.explanation}</p>
                  ) : (
                    <div className="space-y-3">
                      {[100, 85, 60].map((w, i) => (
                        <div key={i} className={`h-4 bg-slate-200/70 rounded-full animate-pulse`} style={{ width: `${w}%` }} />
                      ))}
                      <p className="text-sm text-slate-400 pt-2">AI explanation will appear here after connecting the API.</p>
                    </div>
                  )}
                </div>
              </Section>

              {/* ── Questions to Ask Your Doctor [NEW] ── */}
              {/* Hidden automatically when questions array is empty or absent */}
              {result.questions?.length > 0 && (
                <Section>
                  <div className="flex items-start gap-3 mb-5">
                    <div className="w-9 h-9 rounded-xl bg-violet-100 flex items-center justify-center flex-shrink-0 mt-0.5 text-violet-600">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="w-5 h-5">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M8.625 12a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 01-2.555-.337A5.972 5.972 0 015.41 20.97a5.969 5.969 0 01-.474-.065 4.48 4.48 0 00.978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25z" />
                      </svg>
                    </div>
                    <div>
                      <h2 className="text-lg font-bold text-slate-800" style={{ fontFamily: "'DM Serif Display', serif" }}>
                        Questions to Ask Your Doctor
                      </h2>
                      <p className="text-sm text-slate-500 mt-0.5">
                        Bring these to your next appointment — your doctor can give you personalised answers.
                      </p>
                    </div>
                  </div>

                  <ul className="space-y-3">
                    {result.questions.map((q, i) => (
                      <li key={i} className="flex items-start gap-3 p-3.5 rounded-xl bg-violet-50 border border-violet-100">
                        <span className="flex-shrink-0 w-6 h-6 rounded-full bg-violet-200 text-violet-700 text-xs font-bold flex items-center justify-center mt-0.5">
                          {i + 1}
                        </span>
                        <p className="text-sm text-slate-700 leading-relaxed">{q}</p>
                      </li>
                    ))}
                  </ul>

                  <p className="mt-4 text-xs text-slate-400 flex items-center gap-1.5">
                    <InfoIcon />
                    These questions are for informational purposes only and do not constitute medical advice.
                  </p>
                </Section>
              )}
            </>
          )}
        </main>

        {/* ── Footer Disclaimer ── */}
        <footer className="border-t border-slate-100 bg-white/60 mt-10">
          <div className="max-w-5xl mx-auto px-6 py-8">
            <div className="flex flex-col md:flex-row items-start md:items-center gap-4 p-5 bg-amber-50 rounded-2xl border border-amber-200">
              <div className="w-10 h-10 rounded-xl bg-amber-100 flex items-center justify-center flex-shrink-0">
                <DoctorIcon />
              </div>
              <div className="flex-1">
                <p className="text-sm font-semibold text-amber-800">Not a Medical Diagnosis</p>
                <p className="text-sm text-amber-700 mt-0.5 leading-relaxed">
                  This tool is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.
                  Always consult a qualified healthcare provider with any questions about your health or lab results.
                </p>
              </div>

            </div>

            <div className="mt-6 flex flex-col md:flex-row justify-between items-center gap-2 text-xs text-slate-400">
              <span>© 2025 Lab Report Intelligence · All data processed locally</span>
              <div className="flex gap-4">
                <a href="#" className="hover:text-slate-600 transition-colors">Privacy Policy</a>
                <a href="#" className="hover:text-slate-600 transition-colors">Terms of Use</a>
                <a href="#" className="hover:text-slate-600 transition-colors">Contact</a>
              </div>
            </div>
          </div>
        </footer>
      </div>
    </>
  );
}