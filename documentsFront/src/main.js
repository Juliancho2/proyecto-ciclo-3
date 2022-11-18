import { createApp } from 'vue'
import {createRouter,createWebHistory,} from 'vue-router'
import App from './App.vue'
import './assets/main.css'
import ListDocuments from './components/ListDocuments.vue'
import Home from './components/Home.vue'
import Record from './components/Record.vue'
import Login from '@/components/Login.vue'



//componentes

// definir rutas


const routes=[
    {
        path:'/',component:Home,name:"home"
        
    },
    {
        path:'/login',component:Login,name:"login"
        
    },
    {
        path:'/inventario',component:ListDocuments,name:"inventario"
        
    },
    {
        path:'/historial',component:Record,name:"historial"
        
    },
    
]


const router= createRouter({
    history:createWebHistory(),
    routes,
})

const app= createApp(App)
app.use(router)
app.mount('#app')


