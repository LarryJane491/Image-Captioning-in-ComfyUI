from .LoRAcaption import LoRACaptionSave, LoRACaptionLoad

NODE_CLASS_MAPPINGS = {
    "LoRA Caption Save": LoRACaptionSave,
	"LoRA Caption Load": LoRACaptionLoad,
}

NODE_DISPLAY_NAME_MAPPINGS = {
 
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']