<template>
    <AppLayout title="__Title__">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 leading-tight">
                __Title__
            </h2>
        </template>

        <div class="py-12">
            <div class="container">
                <div class="card">
                    <div class="card-body">
                        <div class="mb-3">
                            <a
                                class="btn btn-primary"
                                :href="route('admin.__table__.add')"
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
                                <tr v-for="item in __table__" :key="item.id">
                                    <td>{{ item.__field__ }}</td>

                                    <td>
                                        <jet-primary-button
                                            ><a
                                                :href="
                                                    route(
                                                        'admin.__table__.details',
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
                                                        'admin.__table__.edit',
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
        __table__: {
            type: Array,
        },
    },

    setup() {
        const form = useForm({});

        const delete_item = (__table__) => {
            if (confirm("Are you sure you want to delete this __table__?")) {
                form.delete(route("admin.__table__.delete", __table__.id));
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
