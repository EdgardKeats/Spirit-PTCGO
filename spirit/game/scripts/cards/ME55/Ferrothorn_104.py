from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d21b160c-1305-5cfa-955e-d2f590821f9e",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn", "Stage 1", "Ferrothorn"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    family_id=598,
    abilities=[
        Attack(
            title="Spike Sting",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Kaboom Needles",
            game_text="This attack does 50 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) This Pok\u00e9mon also does 130 damage to itself.",
            cost={PokemonTypes.METAL: 2},
            effect=unimplemented,
        ),
    ],
)