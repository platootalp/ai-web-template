<template>
  <!-- genAI_master_start -->
  <main class="mx-auto flex min-h-screen w-full max-w-4xl flex-col gap-8 px-6 py-12">
    <header class="space-y-2">
      <p class="text-sm uppercase tracking-[0.3em] text-slate-400">
        AI Agent Vue Template
      </p>
      <h1 class="text-3xl font-semibold text-white">
        前后端分离的 AI Agent Vue 模板
      </h1>
      <p class="text-base text-slate-300">
        使用 Vue + TanStack Query 调用 FastAPI + LangChain 的 Agent 服务。
      </p>
    </header>

    <ChatCard title="发送消息">
      <form class="space-y-4" @submit.prevent="handleSubmit">
        <textarea
          v-model="message"
          class="min-h-[120px] w-full rounded-xl border border-slate-700 bg-slate-950 p-4 text-sm text-slate-100 placeholder:text-slate-600 focus:border-blue-500 focus:outline-none"
          placeholder="输入要发送给 Agent 的消息..."
          required
        />
        <button
          class="rounded-xl bg-blue-500 px-6 py-2 text-sm font-semibold text-white transition hover:bg-blue-400 disabled:cursor-not-allowed disabled:bg-slate-600"
          type="submit"
          :disabled="isPending"
        >
          {{ isPending ? "生成中..." : "发送" }}
        </button>
      </form>
    </ChatCard>

    <ChatCard title="Agent 回复">
      <p
        v-if="error"
        class="rounded-lg border border-red-500/40 bg-red-500/10 p-3 text-red-200"
      >
        请求失败，请稍后重试。
      </p>
      <p v-else-if="!data" class="text-slate-400">提交消息后将在此处显示回复。</p>
      <p v-else class="whitespace-pre-wrap rounded-lg bg-slate-950 p-4 text-slate-100">
        {{ data.reply }}
      </p>
    </ChatCard>
  </main>
  <!-- genAI_master_end -->
</template>

<script setup lang="ts">
/** genAI_master_start */
import { ref } from "vue";

import ChatCard from "../components/ChatCard.vue";
import { useAgentChat } from "../composables/useAgentChat";

const message = ref("");
const { mutateAsync, data, isPending, error } = useAgentChat();

const handleSubmit = async () => {
  if (!message.value.trim()) {
    return;
  }
  await mutateAsync(message.value.trim());
};
/** genAI_master_end */
</script>
