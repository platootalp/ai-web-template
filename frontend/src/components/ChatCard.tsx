/** genAI_master_start */
import type { ReactNode } from "react";

type ChatCardProps = {
  title: string;
  children: ReactNode;
};

function ChatCard({ title, children }: ChatCardProps) {
  return (
    <section className="rounded-2xl bg-slate-900/70 p-6 shadow-xl shadow-black/20">
      <h2 className="text-lg font-semibold text-slate-100">{title}</h2>
      <div className="mt-4 space-y-3 text-sm text-slate-200">{children}</div>
    </section>
  );
}

export default ChatCard;
/** genAI_master_end */
