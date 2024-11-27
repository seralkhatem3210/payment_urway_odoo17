# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
# from . import hooks  # If hooks are defined in a separate file
# from .hooks import post_init_hook  # Ensure this line is present


# from odoo.addons.payment import setup_provider, reset_payment_provider


# # def post_init_hook(cr, registry):
# #     setup_provider(cr, registry, 'urway')

# def post_init_hook(cr, registry):
#     """
#     Logic executed after the module is installed.
#     """
#     # Example: Add initial setup or data processing here
#     env = api.Environment(cr, SUPERUSER_ID, {})
#     # Your post-installation logic here, such as updating records
#     setup_provider(cr, registry, 'urway')


# def uninstall_hook(cr, registry):
#     reset_payment_provider(cr, registry, 'urway')
