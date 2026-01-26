import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const roastGithub = async (username: string, intensity: "mild" | "medium" | "savage" = "mild") => {
  const res = await axios.post(`${API_URL}/api/roast/github`, { username, intensity });
  return res.data;
};
