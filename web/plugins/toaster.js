import { useToast } from 'vue-toast-notification'

const toast = useToast()

// eslint-disable-next-line no-undef
export default defineNuxtPlugin(() => {
  return {
    provide: {
      toast
    }
  }
})
