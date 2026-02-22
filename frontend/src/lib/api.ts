import axios from "axios";

const API_URL = "https://roast-my-profile-backend.onrender.com";

export const roastGithub = async (username: string, intensity: "mild" | "medium" | "savage" = "mild") => {
  const res = await axios.post(`${API_URL}/api/roast/github`, { username, intensity });
  return res.data;
};
