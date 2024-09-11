import Home from '../pages/home.js'

const routes = [
    { path : '/', component : Home}
]

const router = new VueRouter({
    routes
})

export default router