<template>
    <div class="bg-gray-50 min-h-screen">

        <!-- Header -->
        <section class="max-w-6xl mx-auto px-4 py-6">
            <div class="max-w-5xl">

                <h1 class="text-3xl md:text-5xl font-semibold text-gray-900">
                    Explore the Best {{ route.params.type }} for Sale in Bangalore
                </h1>

                <!-- <div class="w-24 h-1 bg-teal-500 rounded mt-4 mb-8"></div> -->

                <p class="text-gray-600 text-lg leading-10">
                    Bangalore's property market is among the fastest-growing in India,
                    offering a wide range of premium apartments and modern residential
                    developments designed to suit contemporary lifestyles. Whether you are
                    a professional seeking excellent connectivity to major business districts
                    or a family looking for peaceful, green, and well-developed neighborhoods,
                    Bangalore provides numerous housing options to meet your needs.
                </p>

                <p class="text-gray-600 text-lg leading-10 mt-8">
                    Our platform makes your home search easier by showcasing new launch
                    apartments, pre-launch projects, upcoming developments, under-construction
                    properties, and ready-to-move-in homes from trusted builders. Every listing
                    is carefully verified and regularly updated with essential details such as
                    floor plans, pricing information, special launch offers, amenities, and
                    current availability to help you make an informed decision.
                </p>

            </div>
        </section>
        <!-- Projects -->
        <section class="max-w-6xl mx-auto px-8 pb-10">

            <div v-for="project in projects" :key="project.name" class="bg-[#f5f5f5] rounded-3xl overflow-hidden mb-8">
                <div class="grid md:grid-cols-[40%_60%]">

                    <!-- Image -->
                    <div>
                        <img :src="project.thumbnail_image" :alt="project.project_name"
                            class="w-full h-[300px] object-cover" />
                    </div>

                    <!-- Content -->
                    <div class="p-8 flex flex-col justify-between">

                        <div>
                            <h2 class="text-2xl md:text-3xl font-semibold mb-4">
                                {{ project.project_name }}
                            </h2>

                            <p class="text-gray-600 text-lg">
                                {{ getShortDescription(project.description) }}
                            </p>
                        </div>

                        <div>
                            <div class="space-y-2 text-lg mt-6">
                                <p>
                                    <span class="font-semibold">Location:</span>
                                    {{ project.full_location }}
                                </p>

                                <p>
                                    <span class="font-semibold">BHK:</span>
                                    {{ project.bhk }}
                                </p>

                                <p>
                                    <span class="font-semibold">Status:</span>
                                    {{ project.status }}
                                </p>
                            </div>

                            <div class="flex gap-4 mt-6">
                                <router-link :to="`/project/${project.url}`"
                                    class="px-8 py-3 border rounded-xl hover:bg-gray-100">
                                    View Project
                                </router-link>

                                <button class="px-8 py-3 bg-green-600 text-white rounded-xl hover:bg-teal-600">
                                    Get Pricing
                                </button>
                            </div>
                        </div>

                    </div>

                </div>
            </div>

            <div v-if="projects.length === 0" class="text-center py-10 text-gray-500">
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

    return text.split(" ").slice(0, 10).join(" ") + "...";
};

const getProjects = async () => {
    try {
        const propertyType = route.params.type;

        const response = await fetch(
            `/api/method/per_sqr_ft.api.property.get_projects_by_type?property_type=${propertyType}`
        );

        const data = await response.json();

        projects.value = data.message || [];
    } catch (error) {
        console.error("Error fetching projects:", error);
    }
};

onMounted(() => {
    getProjects();
});
</script>
