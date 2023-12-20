/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";

export class TakeAwayButton extends ProductScreen {
    static template = "TakeAwayButton";

    setup() {
        this.pos = usePos();
        this.orm = useService("orm");

    }

    async onClick() {
        try {
            console.log("TakeAwayButton onClick");

            // Set takeaway value on the order
            const order = this.pos.get_order();
            order.set_takeaway(true);
            order.takeawayButtonClicked = true;

            // Call the generate_token function on the server using useService
            const uid = order.uid;  // Replace 'uid' with the actual property name that stores the order's UID
            const result = await this.orm.call("pos.config", "generate_token", [uid]);
            console.log("RPC Result:", result);
            console.log("Generated Token:", result);


            // Add additional logic based on the response if needed
        } catch (error) {
            console.log("Error calling generate_token:", error);
            console.log("Error Response:", error.data); // Log the error response

            // Handle the error, e.g., show a user-friendly message
            // You may want to notify the user or take appropriate action
        }
    }
}

ProductScreen.addControlButton({
    component: TakeAwayButton,
    condition: function () {
        console.log("Condition Check:", this.pos.config.is_takeaway);
        return this.pos.config.is_takeaway;
    },
    position: ['before', 'OrderlineCustomerNoteButton']
});
