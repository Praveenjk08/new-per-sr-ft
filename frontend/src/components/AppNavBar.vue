<template>
  <header class="sticky top-0 left-0 w-full z-50 bg-white shadow-sm">
    <div class="max-w-[1400px] mx-auto">

      <!-- Navbar -->
      <nav class="flex items-center h-[85px] px-4 lg:px-10">

        <!-- Logo -->
        <div class="flex items-center gap-2">
          <router-link to="/">
            <img
              src="/files/homelogoe.jpg"
              alt="Logo"
              class="h-[60px] object-contain"
            />
          </router-link>
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden lg:flex items-center gap-10 ml-auto">

          <router-link to="/" class="nav-link focus:outline-none focus:ring-0">
            Per Square Feet
          </router-link>

          <router-link to="/about-us" class="nav-link">
            About Us
          </router-link>

          <!-- Services Dropdown -->
          <div class="relative group">

            <button class="nav-link flex items-center gap-1">
              Services

              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-4 h-4"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
                />
              </svg>
            </button>

            <div
              class="absolute top-full left-0 mt-2 bg-white shadow-lg rounded-xl py-3 w-80 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50"
            >

              <router-link
                to="/construction"
                class="nav-link-service-project block px-5 py-3 hover:bg-blue-50"
              >
                Construction
              </router-link>

              <router-link
                to="/interior"
                class="nav-link-service-project block px-5 py-3 hover:bg-blue-50"
              >
                Interior
              </router-link>
              <router-link
                to="/real estate consultation"
                class="nav-link-service-project block px-5 py-3 hover:bg-blue-50"
              >
                Real Estate Consultation
              </router-link>
                 <router-link
                to="/housing-loan"
                class="nav-link-service-project block px-5 py-3 hover:bg-blue-50"
              >
                Housing Loan Services
              </router-link>
                 <router-link
                to="/legal"
                class="nav-link-service-project block px-5 py-3 hover:bg-blue-50"
              >
               Legal Consultation
              </router-link>
                 <router-link
                to="/property-management"
                class="nav-link-service-project block px-5 py-3 hover:bg-blue-50"
              >
               Property Management
              </router-link>

            </div>
          </div>

          <!-- Projects Dropdown -->
          <div class="relative group">

            <button class="nav-link flex items-center gap-1">
              Projects

              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-4 h-4"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
                />
              </svg>
            </button>

            <div
              class="absolute top-full left-0 mt-2 bg-white shadow-lg rounded-xl py-3 w-52 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50"
            >

              <router-link
                to="/new-projects"
                class="nav-link-service-project block px-5 py-3 hover:bg-blue-50"
              >
                New Projects
              </router-link>

              <router-link
                to="/projects/Ongoing"
                class="nav-link-service-project block px-5 py-3 hover:bg-blue-50"
              >
                Ongoing Projects
              </router-link>

              <router-link
                to="/projects/Upcoming"
                class="nav-link-service-project block px-5 py-3 hover:bg-blue-50"
              >
                Upcoming Projects
              </router-link>

              <router-link
                to="/projects/Completed"
                class="nav-link-service-project block px-5 py-3 hover:bg-blue-50"
              >
                Completed Projects
              </router-link>

            </div>
          </div>

          <!-- <router-link to="/blog" class="nav-link">
            Gallery
          </router-link> -->

          <router-link to="/contact-us" class="nav-link">
            Contact
          </router-link>

          <!-- Login Button -->
          <button
            @click="goToLogin"
            class="ml-4 bg-[#156082] hover:bg-[#0B1560] text-white px-6 py-2 rounded-xl text-[16px] font-medium transition-all duration-300 shadow-md"
          >
            Login
          </button>

        </div>

        <!-- Mobile Menu Button -->
        <div class="lg:hidden ml-auto">

          <button @click="toggleMenu">

            <svg
              class="w-7 h-7 text-[#156082]"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >

              <path
                v-if="!isOpen"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />

              <path
                v-else
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />

            </svg>

          </button>

        </div>

      </nav>

      <!-- Mobile Menu -->
      <transition name="fade-slide">

        <div
          v-if="isOpen"
          class="lg:hidden bg-white border-t border-gray-200 px-6 py-6"
        >

          <ul class="flex flex-col space-y-5">

            <li>
              <router-link
                to="/"
                class="mobile-link"
                @click="closeMenu"
              >
                Per Square Feet
              </router-link>
            </li>

            <li>
              <router-link
                to="/about-us"
                class="mobile-link"
                @click="closeMenu"
              >
                About Us
              </router-link>
            </li>

            <!-- Services -->
            <li>

              <button
                @click="toggleServices"
                class="w-full flex items-center text-[18px] font-medium text-[#156082]"
              >

                <span>Services</span>

                <span
                  :class="{ 'rotate-180': isServicesOpen }"
                  class="transition duration-300 ml-auto"
                >

                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="w-5 h-5"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z"
                      clip-rule="evenodd"
                    />
                  </svg>

                </span>

              </button>

              <ul v-show="isServicesOpen" class="mt-3 ml-4 space-y-3">

                <li>
                  <router-link
                    to="/construction"
                    class="block text-[18px] font-medium text-[#156082] no-underline"
                    @click="closeMenu"
                  >
                    Construction
                  </router-link>
                </li>

                <li>
                  <router-link
                    to="/interiors"
                    class="block text-[18px] font-medium text-[#156082] no-underline"
                    @click="closeMenu"
                  >
                    Interiors
                  </router-link>
                </li>
                 <li>
                  <router-link
                    to="/real estate consultation"
                    class="block text-[18px] font-medium text-[#156082] no-underline"
                    @click="closeMenu"
                  >
                    Real Estate Consultation
                  </router-link>
                </li>
                 <li>
                  <router-link
                    to="/housing-loan"
                    class="block text-[18px] font-medium text-[#156082] no-underline"
                    @click="closeMenu"
                  >
                   Housing Loan Services
                  </router-link>
                </li>
                 <li>
                  <router-link
                    to="/legal"
                    class="block text-[18px] font-medium text-[#156082] no-underline"
                    @click="closeMenu"
                  >
                    Legal Consultation
                  </router-link>
                </li>
                 <li>
                  <router-link
                    to="/property-management"
                    class="block text-[18px] font-medium text-[#156082] no-underline"
                    @click="closeMenu"
                  >
                   Property Management
                  </router-link>
                </li>

              </ul>

            </li>

            <!-- Projects -->
            <li>

              <button
                @click="toggleProjects"
                class="w-full flex items-center text-[18px] font-medium text-[#156082]"
              >

                <span>Projects</span>

                <span
                  :class="{ 'rotate-180': isProjectsOpen }"
                  class="transition duration-300 ml-auto"
                >

                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="w-5 h-5"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z"
                      clip-rule="evenodd"
                    />
                  </svg>

                </span>

              </button>

              <ul v-show="isProjectsOpen" class="mt-3 ml-4 space-y-3">

                <li>
                  <router-link
                    to="/new-projects"
                    class="block text-[18px] font-medium text-[#156082] no-underline"
                    @click="closeMenu"
                  >
                    New Projects
                  </router-link>
                </li>

                <li>
                  <router-link
                    to="/projects/Ongoing"
                    class="block text-[18px] font-medium text-[#156082] no-underline"
                    @click="closeMenu"
                  >
                    Ongoing Projects
                  </router-link>
                </li>

                <li>
                  <router-link
                    to="/projects/Upcoming"
                    class="block text-[18px] font-medium text-[#156082] no-underline"
                    @click="closeMenu"
                  >
                    Upcoming Projects
                  </router-link>
                </li>

                <li>
                  <router-link
                    to="/projects/Completed"
                    class="block text-[18px] font-medium text-[#156082] no-underline"
                    @click="closeMenu"
                  >
                    Completed Projects
                  </router-link>
                </li>

              </ul>

            </li>

            <li>
              <router-link
                to="/blog"
                class="mobile-link"
                @click="closeMenu"
              >
                Gallery
              </router-link>
            </li>

            <li>
              <router-link
                to="/contact-us"
                class="mobile-link"
                @click="closeMenu"
              >
                Contact
              </router-link>
            </li>

            <!-- Mobile Login Button -->
            <li>

              <button
                @click="goToLogin"
                class="w-full bg-[#156082] hover:bg-[#0B1560] text-white py-3 rounded-xl text-[18px] font-medium transition duration-300"
              >
                Login
              </button>

            </li>

          </ul>

        </div>

      </transition>

    </div>
  </header>
</template>

<script setup>
import { ref } from "vue";

const isOpen = ref(false);
const isServicesOpen = ref(false);
const isProjectsOpen = ref(false);

const toggleMenu = () => {
  isOpen.value = !isOpen.value;
};

const closeMenu = () => {
  isOpen.value = false;
};

const toggleServices = () => {
  isServicesOpen.value = !isServicesOpen.value;
};

const toggleProjects = () => {
  isProjectsOpen.value = !isProjectsOpen.value;
};

const goToLogin = () => {
  window.location.href = "/login";
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

* {
  font-family: 'Poppins', sans-serif;
}

.nav-link {
  color: #156082;
  text-decoration: none;
  font-size: 18px;
  font-weight: 400;
  transition: all 0.3s ease;
}

.nav-link:hover {
  color: #0e4d67;
}

.nav-link-service-project {
  color: #156082;
  text-decoration: none;
  font-size: 16px;
}

.mobile-link {
  color: #156082;
  text-decoration: none;
  font-size: 18px;
  font-weight: 500;
  display: block;
}

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.3s ease;
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>