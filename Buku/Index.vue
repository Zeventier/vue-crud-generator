<template>
    <AppLayout title="Buku">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 leading-tight">
                Buku
            </h2>
        </template>

        <div class="py-12">
            <div class="container">
                <div class="card">
                    <div class="card-body">
                        <div class="mb-3">
                            <a
                                class="btn btn-primary"
                                :href="route('admin.buku.add')"
                                ><font-awesome-icon
                                    icon="fa-solid fa-square-plus"
                                />
                                &nbsp; Buat baru</a
                            >
                        </div>
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>__Field__</th>

                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in buku" :key="item.id">
                                    <td>{{ item.__field__ }}</td>

                                    <td>
                                        <jet-primary-button
                                            ><a
                                                :href="
                                                    route(
                                                        'admin.buku.details',
                                                        item
                                                    )
                                                "
                                                ><font-awesome-icon
                                                    icon="fa-solid fa-magnifying-glass" /></a
                                        ></jet-primary-button>
                                        &nbsp;
                                        <jet-secondary-button
                                            ><a
                                                :href="
                                                    route(
                                                        'admin.buku.edit',
                                                        item
                                                    )
                                                "
                                                ><font-awesome-icon
                                                    icon="fa-solid fa-pen-to-square" /></a
                                        ></jet-secondary-button>
                                        &nbsp;
                                        <jet-danger-button
                                            @click="delete_item(item)"
                                        >
                                            <a
                                                ><font-awesome-icon
                                                    icon="fa-solid fa-trash-can"
                                            /></a>
                                        </jet-danger-button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </AppLayout>
</template>

<script>
import { useForm } from "@inertiajs/vue3";
import AppLayout from "@/Layouts/AppLayout.vue";
import JetDangerButton from "@/Components/DangerButton.vue";
import JetPrimaryButton from "@/Components/PrimaryButton.vue";
import JetSecondaryButton from "@/Components/SecondaryButton.vue";

export default {
    components: {
        AppLayout,
        JetDangerButton,
        JetPrimaryButton,
        JetSecondaryButton,
    },

    props: {
        buku: {
            type: Array,
        },
    },

    setup() {
        const form = useForm({});

        const delete_item = (buku) => {
            if (confirm("Are you sure you want to delete this buku?")) {
                form.delete(route("admin.buku.delete", buku.id));
            }
        };

        return {
            form,
            delete_item,
        };
    },
};
</script>

<style></style>
