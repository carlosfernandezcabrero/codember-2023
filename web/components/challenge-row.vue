<template>
  <tr class="text-base">
    <td class="px-6 py-3 font-medium">{{ challenge.name }}</td>
    <td v-if="!pending" class="px-6 py-3 text-center">
      {{ challengeResolve.elapsed_time }} ms
    </td>
    <td v-if="pending" class="px-6 py-3">
      <div class="h-2.5 bg-gray-300 rounded-full w-[4ch] mx-auto"></div>
    </td>
    <td
      v-if="!pending"
      class="py-3 px-6 max-w-[30ch]"
      :class="{
        'text-red-600 font-bold uppercase animate-pulse':
          challengeResolve.execution_return === 'fail'
      }"
    >
      <template v-if="challengeResolve.execution_return === 'fail'">
        error
      </template>
      <div
        v-if="challengeResolve.execution_return === 'success'"
        class="flex items-center justify-between gap-x-2"
      >
        <span class="truncate">
          {{ challengeResolve.output }}
        </span>
        <button
          class="text-gray-700 hover:text-indigo-600 active:scale-110"
          @click="copyToClipboard"
        >
          <IconsCopy />
        </button>
      </div>
    </td>
    <td v-if="pending" class="px-6 py-3 font-bold text-gray-400 uppercase">
      Cargando ...
    </td>
    <td class="px-6 py-3 text-center">
      <a
        :href="`${apiUrl}/${challenge.input_path}`"
        target="_blank"
        rel="noopener noreferrer"
        class="font-medium text-blue-600 hover:underline"
      >
        Descargar
      </a>
    </td>
    <td class="px-6 py-3 text-center">
      <a
        :href="`${apiUrl}/${challenge.code}`"
        target="_blank"
        rel="noopener noreferrer"
        class="font-medium text-blue-600 hover:underline"
      >
        Ver
      </a>
    </td>
    <td class="px-6 py-3 text-center">
      <button
        class="font-medium text-blue-600 align-middle hover:underline disabled:cursor-not-allowed"
        @click="setIsOpen"
        :disabled="pending"
      >
        Ver
      </button>
    </td>
    <td class="px-6 py-3 text-center">
      <button class="align-middle group active:scale-110" @click="refresh">
        <IconsPlay />
      </button>
    </td>
  </tr>
  <Dialog :open="isOpen" @close="() => setIsOpen(true)">
    <div class="fixed inset-0 bg-black/30" aria-hidden="true" />
    <div class="fixed inset-0 flex items-center justify-center w-screen p-4">
      <DialogPanel class="bg-white divide-y rounded-lg">
        <DialogTitle
          :class="`text-4xl font-bold p-6 flex items-center gap-x-5 ${
            challengeResolve.execution_return === 'fail'
              ? 'text-red-600'
              : 'text-green-600'
          }`"
        >
          <span>
            {{ challengeResolve.execution_return === 'fail' ? '❌' : '✅' }}
          </span>
          {{ challengeResolve.execution_return }}
        </DialogTitle>

        <div class="p-6">
          <pre
            >{{
              challengeResolve.execution_return === 'fail'
                ? challengeResolve.log
                : 'OK'
            }}
        </pre
          >
        </div>

        <footer class="p-6 text-center">
          <button
            type="button"
            class="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-lg text-sm px-5 py-2.5"
            @click="setIsOpen(false)"
          >
            OK
          </button>
        </footer>
      </DialogPanel>
    </div>
  </Dialog>
</template>

<script setup>
import { Dialog, DialogPanel, DialogTitle } from '@headlessui/vue'

const { challenge } = defineProps({
  challenge: {
    required: true
  }
})

const isOpen = ref(false)
const { $toast } = useNuxtApp()
const { apiUrl } = useRuntimeConfig().public

function setIsOpen(value) {
  isOpen.value = value
}

async function copyToClipboard() {
  $toast.info('Copiado al portapapeles 🥳 !!!', {
    position: 'top'
  })
  await navigator.clipboard.writeText(challengeResolve.value.output)
}

const {
  data: challengeResolve,
  pending,
  refresh
} = await useFetch(`${apiUrl}/challenge/${challenge.name}`, {
  server: false,
  lazy: true
})
</script>
