"use client";
import { useState } from "react";
import { roastGithub } from "@/lib/api";

export default function RoastPage() {
  const [username, setUsername] = useState("");
  const [roast, setRoast] = useState("");

  const handleSubmit = async () => {
    const res = await roastGithub(username);
    setRoast(res?.roast || "No roast found 😅");
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-black text-white">
      <h1 className="text-4xl font-bold mb-6">🔥 GitHub Roast Machine</h1>
      <input
        type="text"
        placeholder="Enter your GitHub username..."
        className="p-3 rounded-lg text-black w-80 mb-4"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <button
        onClick={handleSubmit}
        className="bg-red-600 hover:bg-red-700 px-5 py-2 rounded-lg font-semibold"
      >
        Roast Me 😎
      </button>

      {roast && (
        <div className="mt-6 p-4 bg-gray-800 rounded-lg w-96 text-center">
          <p>{roast}</p>
        </div>
      )}
    </div>
  );
}
