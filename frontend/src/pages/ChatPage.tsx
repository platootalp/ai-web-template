/** genAI_master_start */
import { useState } from "react";

import ChatCard from "../components/ChatCard";
import { useAgentChat } from "../hooks/useAgentChat";

function ChatPage() {
  const [message, setMessage] = useState("");
  const { mutateAsync, data, isPending, error } = useAgentChat();

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!message.trim()) {
      return;
    }
    await mutateAsync(message.trim());
  };

  return (
    <main className="mx-auto flex min-h-screen w-full max-w-4xl flex-col gap-8 px-6 py-12">
      <header className="space-y-2">
        <p className="text-sm uppercase tracking-[0.3em] text-slate-400">
          AI Agent Template
        </p>
        <h1 className="text-3xl font-semibold text-white">
          前后端分离的 AI Agent 项目模板
        </h1>
        <p className="text-base text-slate-300">
          使用 React + TanStack Query 调用 FastAPI + LangChain 的 Agent 服务。
        </p>
      </header>

      <ChatCard title="发送消息">
        <form className="space-y-4" onSubmit={handleSubmit}>
          <textarea
            className="min-h-[120px] w-full rounded-xl border border-slate-700 bg-slate-950 p-4 text-sm text-slate-100 placeholder:text-slate-600 focus:border-blue-500 focus:outline-none"
            placeholder="输入要发送给 Agent 的消息..."
            value={message}
            onChange={(event) => setMessage(event.target.value)}
            required
          />
          <button
            className="rounded-xl bg-blue-500 px-6 py-2 text-sm font-semibold text-white transition hover:bg-blue-400 disabled:cursor-not-allowed disabled:bg-slate-600"
            type="submit"
            disabled={isPending}
          >
            {isPending ? "生成中..." : "发送"}
          </button>
        </form>
      </ChatCard>

      <ChatCard title="Agent 回复">
        {error && (
          <p className="rounded-lg border border-red-500/40 bg-red-500/10 p-3 text-red-200">
            请求失败，请稍后重试。
          </p>
        )}
        {!data && !error && (
          <p className="text-slate-400">提交消息后将在此处显示回复。</p>
        )}
        {data && (
          <p className="whitespace-pre-wrap rounded-lg bg-slate-950 p-4 text-slate-100">
            {data.reply}
          </p>
        )}
      </ChatCard>
    </main>
  );
}

export default ChatPage;
/** genAI_master_end */
