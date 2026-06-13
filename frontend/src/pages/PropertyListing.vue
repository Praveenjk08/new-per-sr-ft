<template>
    <div class="bg-gray-50 min-h-screen mb-0">

        <section
            class="max-w-7xl mx-auto px-4 py-10 md:py-16 mb-10 bg-gradient-to-r from-blue-900 via-blue-800 to-cyan-700 overflow-hidden relative">

            <!-- Background Blur -->
            <div class="absolute top-0 right-0 w-72 h-72 bg-cyan-400/20 rounded-full blur-3xl">
            </div>

            <div class="absolute bottom-0 left-0 w-72 h-72 bg-orange-400/20 rounded-full blur-3xl">
            </div>

            <div class="relative z-10 max-w-5xl">

                <span class="inline-block px-4 py-2 bg-white/20 text-white rounded-full text-sm font-medium mb-4">
                    Premium Properties in Bangalore
                </span>

                <h1 class="text-3xl md:text-6xl font-bold text-white leading-tight">

                    Explore the Best

                    <span class="text-orange-400">
                        {{ route.params.type }}
                    </span>

                    for Sale in Bangalore

                </h1>

                <p class="text-white/90 text-base md:text-xl leading-8 mt-6 max-w-4xl">

                    Bangalore's property market is among the fastest-growing in India,
                    offering premium apartments, villas, gated communities and luxury
                    residential developments across the city.

                </p>

                <p class="text-white/80 text-base md:text-lg leading-8 mt-4 max-w-4xl">

                    Discover verified projects, floor plans, pricing details,
                    launch offers, amenities and availability from trusted builders.

                </p>

                <!-- Stats -->
                <div class="flex flex-wrap gap-6 mt-8">

                    <div class="bg-white/10 backdrop-blur-md rounded-2xl px-6 py-4">
                        <h3 class="text-2xl font-bold text-white">
                            100+
                        </h3>
                        <p class="text-white/80">
                            Projects
                        </p>
                    </div>

                    <div class="bg-white/10 backdrop-blur-md rounded-2xl px-6 py-4">
                        <h3 class="text-2xl font-bold text-white">
                            50+
                        </h3>
                        <p class="text-white/80">
                            Builders
                        </p>
                    </div>

                    <div class="bg-white/10 backdrop-blur-md rounded-2xl px-6 py-4">
                        <h3 class="text-2xl font-bold text-white">
                            1000+
                        </h3>
                        <p class="text-white/80">
                            Happy Buyers
                        </p>
                    </div>

                </div>

            </div>

        </section>
        <!-- Projects -->
        <section class="max-w-5xl mx-auto px-4 md:px-0 pb-10">



            <div v-if="projects.length">



                <div v-for="(project, index) in projects" :key="index"
                    class="bg-white rounded-3xl shadow-sm border overflow-hidden mb-8">

                    <div class="grid md:grid-cols-12">

                        <!-- Image -->
                        <div class="md:col-span-4 p-4">

                            <img :src="project.thumbnail_image" :alt="project.project_name"
                                class="  rounded-lg w-full h-[220px] sm:h-[260px] md:h-[280px] object-cover" />

                        </div>

                        <!-- Content -->
                        <div class="md:col-span-8 p-4 md:p-8 flex flex-col justify-between">

                            <!-- Top -->
                            <div>

                                <h2 class="text-2xl md:text-4xl font-semibold text-gray-900 mb-4">
                                    {{ project.project_name }}
                                </h2>

                                <p class="text-gray-600 text-base md:text-lg leading-7 md:leading-9">
                                    {{ getShortDescription(project.description) }}
                                </p>

                            </div>

                            <!-- Bottom -->
                            <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-6 mt-6">

                                <!-- Details -->
                                <div class="space-y-2 md:space-y-3 text-base md:text-lg">

                                    <p>
                                        <span class="font-semibold">
                                            Location:
                                        </span>
                                        {{ project.full_location }}
                                    </p>

                                    <p>
                                        <span class="font-semibold">
                                            Unit Variants:
                                        </span>
                                        {{ project.unit_variants_lg }}
                                    </p>

                                    <p>
                                        <span class="font-semibold">
                                            Price Range:
                                        </span>

                                        <span class="text-cyan-600 font-semibold">
                                            {{ project.bath }}
                                        </span>
                                    </p>

                                </div>

                                <!-- Buttons -->
                                <div class="flex flex-col sm:flex-row gap-3">

                                    <router-link :to="`/detailpage/${project.url}`"
                                        class="px-6 py-3 border rounded-xl text-center text-base md:text-lg hover:bg-gray-100">
                                        View Project
                                    </router-link>

                                    <router-link :to="`/detailpage/${project.url}`" class="px-6 py-3 bg-yellow-500 text-white rounded-xl text-base md:text-lg
                                       ">

                                        Get Pricing
                                    </router-link>

                                </div>

                            </div>

                        </div>

                    </div>

                </div>


            </div>


            <!-- No Data -->
            <div v-else class="text-center py-10 text-gray-500 text-xl">
                No Projects Found
            </div>


        </section>

    </div>
</template>
<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();

const projects = ref([]);

const getShortDescription = (html) => {
    if (!html) return "";

    const text = html.replace(/<[^>]*>/g, "");

    return text.split(" ").slice(0, 25).join(" ") + "...";
};

const getProjects = async () => {
    try {

        const propertyType = route.params.type;

        const response = await fetch(
            `/api/method/per_sqr_ft.api.property.get_projects_by_type?property_type=${propertyType}`
        );

        const data = await response.json();

        projects.value = data.message || [];

        console.log(projects.value);

    } catch (error) {

        console.error("Error fetching projects:", error);

    }
};

onMounted(() => {
    getProjects();
});
</script>