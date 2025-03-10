import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import pinia from './stores'
import './style.css'

// PrimeVue
import PrimeVue from 'primevue/config'
import 'primevue/resources/themes/lara-light-indigo/theme.css'
import 'primevue/resources/primevue.min.css'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)

app.use(router)
app.use(pinia)
app.use(PrimeVue)
app.use(vuetify)

app.mount('#app')
