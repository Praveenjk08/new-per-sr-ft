import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/PerSquarehome/PersquareHome.vue'),
  },
  {
    path: '/about-us',
    name: 'aboutus',
    component: () => import('@/pages/Aboutus.vue'),
  },
  {
    path: '/contact-us',
    name: 'contact-us',
    component: () => import('@/pages/Contact-us.vue')
  },
  {
    path: '/construction',
    name: 'construction',
    component: () => import('@/services/Construction.vue'),
  },
  {
    path: '/interior',
    name: 'interior',
    component: () => import('@/services/Interior.vue'),
  },
  {
    path: '/real estate consultation',
    name: 'real-estate-consultation',
    component: () => import('@/services/Real Estate Consultation.vue')

  },
  {
    path: '/housing-loan',
    name: 'housing-loan',
    component: () => import('@/services/Housing Loan Services.vue')
  }
  , {
    path: '/legal',
    name: 'legal',
    component: () => import('@/services/Legal Consultation.vue')
  },
  {
    path: '/property-management',
    name: 'property-management',
    component: () => import('@/services/Property Management.vue')

  }
  , {
    path: "/projects",
    name: "projects",
    component: () => import("@/pages/Projects.vue"),
  },

  // {
  //   path: "/project/:slug",
  //   name: "single-project",
  //   component: () => import("@/pages/SingleProject.vue"),
  // },
  {
    path: "/project/:slug",
    name: "detail-project",
    component: () => import("@/pages/DetailProjectpage.vue"),
  },
  {
    path: "/projects/:status",
    name: "projects-by-status",
    component: () => import('@/pages/ProjectsByStatus.vue')
  },

  {
    path: "/search-projects",
    name: "SearchProjects",
    component: () => import("@/pages/SearchProjects.vue"),
  }


]

let router = createRouter({
  history: createWebHistory('/'),
  routes,
  scrollBehavior() {
    return {
      top: 0,
      behavior: 'smooth',
    }
  },
})

export default router
