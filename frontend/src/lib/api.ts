import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const roastGithub = async (username: string) => {
  try {
    const res = await axios.post(`${API_URL}/api/roast/github`, {
      username,
    });
    return res.data;
  } catch (err: any) {
    console.error("Roast error:", err.response?.data || err.message);
  }
};
