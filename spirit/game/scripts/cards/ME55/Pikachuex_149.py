from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4a538f15-6c14-5f18-99c8-a2c5eff1675b",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name",
    display_name="Pikachu ex",
    searchable_by=["Pikachu ex", "Basic", "ex", "Pikachuex"],
    subtypes=["Basic", "ex"],
    collector_number=149,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Pika-Pika Parade",
            game_text="Search your deck for any number of Basic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)