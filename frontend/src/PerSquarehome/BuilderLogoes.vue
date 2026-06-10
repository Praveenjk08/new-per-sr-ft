<template>
    <section class="pb-16 pt-2">

        <div class="bg-[#f7f7f7] sm:rounded-xl py-12 mx-4 lg:mx-4 rounded-3xl">

            <!-- Heading -->
            <div
                class="w-[90%] md:w-full max-w-4xl mx-auto backdrop-blur-3xl bg-gray-200 rounded-2xl shadow-lg p-5 md:p-8 text-center mb-12">

                <h2 class="text-2xl md:text-5xl font-bold leading-tight">
                    Builders Behind
                    <span class="text-orange-600">Exceptional</span>
                    Communities
                </h2>

                <p class="mt-4 text-sm md:text-lg font-medium text-blue-800">
                    Discover Projects from Renowned Property Developers
                </p>

                <div class="w-24 md:w-32 h-[2px] bg-orange-300 mx-auto mt-5"></div>

            </div>

            <!-- Logo Slider -->
            <div class="overflow-hidden relative">

                <div class="flex items-center gap-12 animate-scroll">

                    <!-- Original Logos -->
                    <div v-for="builder in builders" :key="builder.name"
                        class="flex-shrink-0 bg-white rounded-xl p-4 shadow-sm">
                        <img :src="builder.logo" :alt="builder.name" class="h-20 md:h-24 w-[220px] object-contain" />
                    </div>

                    <!-- Duplicate Logos -->
                    <div v-for="builder in builders" :key="'copy-' + builder.name"
                        class="flex-shrink-0 bg-white rounded-xl p-4 shadow-sm">
                        <img :src="builder.logo" :alt="builder.name" class="h-20 md:h-24 w-[220px] object-contain" />
                    </div>

                </div>

            </div>

        </div>

    </section>
</template>

<script setup>
const builders = [
    {
        name: "Deccan Herald",
        logo: "/files/Deccan-Herald-logo-400x124-200x62.png"
    },
    {
        name: "Birla Estates",
        logo: "/files/Aditya_Birla_Group_Logo.svg.png"
    },
    {
        name: "Godrej",
        logo: "/files/godrej-logo-png_seeklogo-61760.png"
    },
    {
        name: "Sobha",
        logo: "/files/Sobha_Developers_Ltd._Corporate_Logo.jpg"
    },
    {
        name: "Puravankara",
        logo: "/files/download.png"
    }
];
</script>

<style scoped>
@keyframes scroll {
    from {
        transform: translateX(0);
    }

    to {
        transform: translateX(-50%);
    }
}

.animate-scroll {
    width: max-content;
    animation: scroll 20s linear infinite;
}

.animate-scroll:hover {
    animation-play-state: paused;
}
</style>