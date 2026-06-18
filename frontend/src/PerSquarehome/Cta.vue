<template>

    <section class="relative py-10 mt-8 overflow-hidden ">
        <div class="bg-[#FAF0E6]">
            <div class="absolute inset-0">
                <img src="/files/HomePageBannerImageNEw-One.jpeg" class="w-full h-full object-cover" />
                <div class="absolute inset-0 bg-black/60"></div>
            </div>

            <div class="relative z-10 max-w-5xl mx-auto text-center px-4">

                <h2 class="text-4xl md:text-5xl font-bold text-white">
                    Ready To Find Your
                    <span class="text-orange-400">
                        Dream Home?
                    </span>
                </h2>

                <p class="text-gray-200 text-lg mt-6 max-w-3xl mx-auto">
                    Explore premium apartments, villas and plots from trusted builders
                    across Bangalore. Let our experts help you find the perfect property.
                </p>

                <div class="flex flex-col sm:flex-row justify-center gap-4 mt-8">

                    <router-link to="/projects"
                        class="bg-orange-500 hover:bg-orange-600 text-white px-8 py-4 rounded-xl font-semibold transition">
                        Explore Projects
                    </router-link>

                    <router-link to="/contact-us"
                        class="bg-white text-gray-900 px-8 py-4 rounded-xl font-semibold hover:bg-gray-100 transition">
                        Contact Us
                    </router-link>

                </div>

            </div>
        </div>

    </section>
</template>