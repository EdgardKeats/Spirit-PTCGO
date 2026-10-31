from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="12d2dd53-73af-5ffb-bbf3-6f6860cb8eee",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Chandelure"],
    subtypes=["Stage 2"],
    collector_number=137,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=609,
    abilities=[
        Attack(
            title="Eerie Glow",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED),
        ),
    ],
)