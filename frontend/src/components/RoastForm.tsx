"use client";
import { useState } from "react";
import { roastGithub } from "../lib/api";

export default function RoastForm({ setRoast }: { setRoast: (r: string) => void }) {
  const [username, setUsername] = useState("");
  const [intensity, setIntensity] = useState<"mild" | "medium" | "savage">("mild");
  const [loading, setLoading] = useState(false);

  async function handleSubmitGithub() {
    if (!username.trim()) return;
    setLoading(true);
    try {
      const res = await roastGithub(username, intensity);
      setRoast(res?.roast || "Something went wrong 😅");
    } catch (error: any) {
      console.error("Roast error:", error);
      if (error.response && error.response.data && error.response.data.detail) {
        setRoast(`Error: ${error.response.data.detail} 🙅‍♂️`);
      } else {
        setRoast("Something went wrong! Is the backend running? �");
      }
    }
    setLoading(false);
  }

  return (
    <div className="flex flex-col gap-6 items-center mt-8">
      <div className="w-full max-w-md bg-gray-800 p-6 rounded-2xl shadow-lg">
        <h2 className="text-xl font-bold mb-4 text-white text-center">🔥 Roast My GitHub</h2>

        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Enter GitHub username"
          className="w-full p-3 rounded bg-gray-700 text-white outline-none focus:ring-2 focus:ring-pink-500"
        />

        <select
          value={intensity}
          onChange={(e) => setIntensity(e.target.value as any)}
          className="w-full mt-3 p-2 rounded bg-gray-700 text-white"
        >
          <option value="mild">Mild 😇</option>
          <option value="medium">Medium 😏</option>
          <option value="savage">Savage 🔥</option>
        </select>

        <button
          onClick={handleSubmitGithub}
          className={`mt-4 w-full py-2 rounded text-white font-semibold transition-all ${loading ? "bg-gray-500 cursor-not-allowed" : "bg-pink-600 hover:bg-pink-700"
            }`}
          disabled={loading}
        >
          {loading ? "Roasting..." : "Roast GitHub 😎"}
        </button>
      </div>
    </div>
  );
}
