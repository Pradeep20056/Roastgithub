"use client";
import { useState } from "react";
import RoastForm from "../components/RoastForm";
import RoastResult from "../components/RoastResult";

export default function Home() {
  const [roast, setRoast] = useState("");

  return (
    <main className="min-h-screen bg-gradient-to-br from-black to-gray-800 text-white flex flex-col items-center p-10">
      <h1 className="text-4xl font-bold mb-4">🔥 Roast My Profile 🔥</h1>
      <p className="text-gray-400 text-center mb-8 max-w-md">
        Enter your GitHub username and get roasted (lovingly) by AI!
      </p>
      <RoastForm setRoast={setRoast} />
      <RoastResult roast={roast} />
    </main>
  );
}
