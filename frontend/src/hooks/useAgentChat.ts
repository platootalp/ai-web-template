/** genAI_master_start */
import { useMutation } from "@tanstack/react-query";

import type { ChatResponse } from "../types";
import { chatWithAgent } from "../services/api";

export const useAgentChat = () => {
  return useMutation({
    mutationFn: (message: string) => chatWithAgent({ message }),
    onError: (error) => {
      const message =
        error instanceof Error ? error.message : "请求失败，请稍后重试。";
      console.warn(message);
    },
  });
};

export type AgentChatResult = ChatResponse;
/** genAI_master_end */
