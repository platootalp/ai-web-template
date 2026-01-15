<template>
  <!-- genAI_master_start -->
  <section class="rounded-2xl bg-slate-900/70 p-6 shadow-xl shadow-black/20">
    <h2 class="text-lg font-semibold text-slate-100">{{ title }}</h2>
    <div class="mt-4 space-y-3 text-sm text-slate-200">
      <slot />
    </div>
  </section>
  <!-- genAI_master_end -->
</template>

<script setup lang="ts">
/** genAI_master_start */
defineProps<{ title: string }>();
/** genAI_master_end */
</script>
