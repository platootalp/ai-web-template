/** genAI_master_start */
import axios from "axios";

import type { ChatRequest, ChatResponse } from "../types";

const api = axios.create({
  baseURL: `${import.meta.env.VITE_API_BASE ?? "http://localhost:8000"}/api/v1`,
});

export const chatWithAgent = async (
  payload: ChatRequest,
): Promise<ChatResponse> => {
  const response = await api.post<ChatResponse>("/chat", payload);
  return response.data;
};
/** genAI_master_end */
