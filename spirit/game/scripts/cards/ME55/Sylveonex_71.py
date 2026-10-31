from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0a5bc41c-16db-549d-b08b-e7515dd10164",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveonex.Name",
    display_name="Sylveon ex",
    searchable_by=["Sylveon ex", "Stage 1", "ex", "Sylveonex"],
    subtypes=["Stage 1", "ex"],
    collector_number=71,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Colorful Harmony",
            game_text="This attack does 50 damage for each type of Basic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)