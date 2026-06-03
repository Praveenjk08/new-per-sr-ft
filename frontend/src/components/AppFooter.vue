<template>
  <footer class="bg-[#0B1560] text-white pt-16 pb-6 mt-20 relative overflow-hidden">

    <!-- Top Border -->
    <div
      class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-blue-500 via-yellow-400 to-blue-500"
    ></div>

    <!-- Main Grid -->
    <div
      class="max-w-7xl mx-auto px-6 lg:px-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12"
    >

      <!-- Logo & About -->
      <div>
        <img
          src="/files/homelogoe.jpg"
          alt="logo"
          class="w-40 mb-5 rounded-full"
        />

        <p class="text-gray-300 leading-7 text-sm">
          Per Square Feet is a modern real estate company helping clients
          discover premium properties with trust, quality, and innovation.
        </p>

        <!-- Social Icons -->
        <div class="flex items-center gap-4 mt-6">

          <!-- Facebook -->
          <a
            href="#"
            class="w-10 h-10 rounded-full border border-gray-500 flex items-center justify-center hover:bg-blue-500 duration-300"
          >
            <i class="ri-facebook-fill text-lg"></i>
          </a>

          <!-- Instagram -->
          <a
            href="#"
            class="w-10 h-10 rounded-full border border-gray-500 flex items-center justify-center hover:bg-pink-500 duration-300"
          >
            <i class="ri-instagram-line text-lg"></i>
          </a>

          <!-- Twitter -->
          <a
            href="#"
            class="w-10 h-10 rounded-full border border-gray-500 flex items-center justify-center hover:bg-sky-500 duration-300"
          >
            <i class="ri-twitter-x-line text-lg"></i>
          </a>

          <!-- LinkedIn -->
          <a
            href="#"
            class="w-10 h-10 rounded-full border border-gray-500 flex items-center justify-center hover:bg-blue-700 duration-300"
          >
            <i class="ri-linkedin-fill text-lg"></i>
          </a>

        </div>
      </div>

      <!-- Quick Links -->
      <div>
        <h2 class="text-2xl font-semibold mb-6">
          Quick Links
        </h2>

        <ul class="space-y-4 text-gray-300">

          <li>
            <router-link
              to="/"
              class="hover:text-yellow-400 duration-300 no-underline text-gray-300"
            >
              Home
            </router-link>
          </li>

          <li>
            <router-link
              to="/about-us"
              class="hover:text-yellow-400 duration-300 no-underline text-gray-300"
            >
              About Us
            </router-link>
          </li>

          <li>
            <router-link
              to="/services"
              class="hover:text-yellow-400 duration-300 no-underline text-gray-300"
            >
              Services
            </router-link>
          </li>

          <li>
            <router-link
              to="/projects"
              class="hover:text-yellow-400 duration-300 no-underline text-gray-300"
            >
              Projects
            </router-link>
          </li>

          <li>
            <router-link
              to="/gallery"
              class="hover:text-yellow-400 duration-300 no-underline text-gray-300"
            >
              Gallery
            </router-link>
          </li>

          <li>
            <router-link
              to="/contact"
              class="hover:text-yellow-400 duration-300 no-underline text-gray-300"
            >
              Contact
            </router-link>
          </li>

        </ul>
      </div>

      <!-- Services -->
      <div>
        <h2 class="text-2xl font-semibold mb-6">
          Our Services
        </h2>

        <ul class="space-y-4 text-gray-300">

          <li class="hover:text-yellow-400 duration-300 cursor-pointer">
            Construction
          </li>

          <li class="hover:text-yellow-400 duration-300 cursor-pointer">
           Real Estate Consultation
          </li>

          <li class="hover:text-yellow-400 duration-300 cursor-pointer">
            Housing Loan Services
          </li>

          <li class="hover:text-yellow-400 duration-300 cursor-pointer">
            Interior Design
          </li>

          <li class="hover:text-yellow-400 duration-300 cursor-pointer">
            Legal Consultation
          </li>
           <li class="hover:text-yellow-400 duration-300 cursor-pointer">
            Property Management
          </li>

        </ul>
      </div>

      <!-- Contact -->
      <div>

        <h2 class="text-2xl font-semibold mb-6">
          Contact Us
        </h2>

        <div class="space-y-5 text-gray-300">

          <!-- Address -->
          <div class="flex items-start gap-3">

            <i class="ri-map-pin-line text-yellow-400 text-xl mt-1"></i>

            <p class="leading-7">
              Bangalore, Karnataka <br />
              India
            </p>

          </div>

          <!-- Phone -->
          <div class="flex items-center gap-3 break-all">

            <i class="ri-phone-line text-yellow-400 text-xl"></i>

            <a
              href="tel:+919686450917"
              class="text-gray-300 no-underline hover:text-yellow-400"
            >
             +91 8884436688 <br>
              +91 9686872201
            </a>
            

          </div>

          <!-- Email -->
          <div class="flex items-center gap-3 break-all">

            <i class="ri-mail-line text-yellow-400 text-xl"></i>

            <a
              href="mailto:info@persquarefeet.com"
              class="text-gray-300 no-underline hover:text-yellow-400"
            >
             kenchagowda.gj@gmail.com
            </a>

          </div>

        </div>

        <!-- Newsletter -->
        <div class="mt-8">

          <h3 class="text-lg mb-3">
            Subscribe Newsletter
          </h3>

          <div class="flex">

            <input
              type="email"
              placeholder="Enter Your Email"
              class="w-full px-4 py-3 rounded-l-full bg-[#13206f] border border-gray-600 outline-none text-sm placeholder:text-gray-400"
            />

            <button
              class="bg-yellow-400 hover:bg-yellow-500 text-black px-6 rounded-r-full font-medium duration-300"
            >
              Send
            </button>

          </div>

        </div>

      </div>
    </div>

    <!-- Bottom -->
    <div
      class="border-t border-gray-700 mt-14 pt-6 flex flex-col md:flex-row justify-between items-center text-gray-400 text-sm px-6 lg:px-12"
    >

      <p>
        © 2026 Per Square Feet. All Rights Reserved.
      </p>

      <p class="mt-3 md:mt-0 underline">
       Powered By:
        <span class="text-yellow-400 font-medium underline">
          Quantumberg Technologies
        </span>
      </p>

    </div>
  </footer>
</template>