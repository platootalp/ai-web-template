/** genAI_master_start */
import { useMutation } from "@tanstack/vue-query";

import { chatWithAgent } from "../services/api";

export const useAgentChat = () => {
  return useMutation({
    mutationFn: (message: string) => chatWithAgent({ message }),
  });
};
/** genAI_master_end */
