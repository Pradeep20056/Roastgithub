export default function RoastResult({ roast }: { roast: string }) {
  if (!roast) return null;
  return (
    <div className="max-w-2xl mx-auto bg-gray-900 text-pink-200 p-6 mt-8 rounded-xl shadow-lg">
      <h2 className="text-xl font-semibold mb-2 text-center">🔥 Your Roast 🔥</h2>
      <p className="whitespace-pre-line text-center">{roast}</p>
    </div>
  );
}
