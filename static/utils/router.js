import Home from '../pages/home.js'
import Login from '../pages/login.js'
import Register from '../pages/register.js'
import {adminDash, influencerDash, sponsorDash, profile} from '../pages/dash.js'

const routes = [
    { path : '/', component : Home},
    { path : '/user-login', component : Login},
    { path : '/register', component : Register },
    {
        path: "/admin-dash",
        component: adminDash,
        meta: { requiresLogin: true, role: "admin" },
    },
    {
        path: "/influencer-dash",
        component: influencerDash,
        meta: { requiresLogin: true, role: "Influencer" },
    },
    {
        path: "/sponsor-dash",
        component: sponsorDash,
        meta: { requiresLogin: true, role: "Sponsor" },
    },
    { path: "/profile", component: profile, meta: { loggedIn: true } },
]

const router = new VueRouter({
    routes
})

export default router