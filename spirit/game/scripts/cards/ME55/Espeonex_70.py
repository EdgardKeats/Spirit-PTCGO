from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bddc7d53-626a-5beb-8bf0-bf1381e6e1bb",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeonex.Name",
    display_name="Espeon ex",
    searchable_by=["Espeon ex", "Stage 1", "ex", "Espeonex"],
    subtypes=["Stage 1", "ex"],
    collector_number=70,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Solar Beatdown",
            game_text="This attack does 30 damage for each of your Pok\u00e9mon in play.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)