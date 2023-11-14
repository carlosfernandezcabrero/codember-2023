<template>
  <header class="flex items-center justify-between py-8">
    <h1 class="text-4xl font-medium">Retos</h1>
    <button
      type="button"
      class="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-lg text-sm px-5 py-2.5 flex items-center gap-x-2"
      @click="() => reloadNuxtApp()"
    >
      <IconsRefresh />
      Recargar
    </button>
  </header>

  <main role="main" class="mt-6">
    <section class="p-4 border border-gray-300 shadow-md rounded-3xl">
      <table class="w-full">
        <thead>
          <tr class="text-xs uppercase bg-slate-200/70">
            <th class="rounded-l-full py-1.5 px-6 text-left">Reto</th>
            <th class="py-1.5 px-6">Tiempo</th>
            <th class="py-1.5 px-6 text-left">salida</th>
            <th class="py-1.5 px-6">input</th>
            <th class="py-1.5 px-6">código</th>
            <th class="py-1.5 px-6">logs</th>
            <th class="rounded-r-full py-1.5 px-6">Ejecutar</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-300">
          <LazyChallengeRow
            v-for="challenge in challenges"
            :challenge="challenge"
          />
        </tbody>
      </table>
    </section>
  </main>

  <footer
    class="flex flex-col px-4 pt-8 pb-8 -mx-4 text-lg text-center text-gray-600 bg-slate-100 gap-y-2"
  >
    <p class="text-base font-semibold tracking-tight">
      Desarrollado por Carlos Fernandez Cabrero 🚀
    </p>
    <a
      href="/"
      target="_blank"
      class="font-medium text-blue-600 underline"
      rel="noopener noreferrer"
    >
      ¡Contribuye al proyecto!
    </a>
  </footer>
</template>

<script setup>
const { apiUrl } = useRuntimeConfig().public
const { data: challenges } = await useFetch(`${apiUrl}/challenges`, {
  server: false
})
</script>
