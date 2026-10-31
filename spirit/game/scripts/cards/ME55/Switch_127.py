from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="01f1514d-aa1e-5224-a1cc-f5bc14df150d",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=127,
    set_code="ME55",
    rarity=Rarities.Common,
    effect=unimplemented
)
