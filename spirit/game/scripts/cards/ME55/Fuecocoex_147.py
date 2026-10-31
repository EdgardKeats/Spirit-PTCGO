from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d6c9aeff-6e2d-5915-a618-8f52b2c2c690",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecocoex.Name",
    display_name="Fuecoco ex",
    searchable_by=["Fuecoco ex", "Basic", "ex", "Fuecocoex"],
    subtypes=["Basic", "ex"],
    collector_number=147,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=909,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Cheerful Flame",
            game_text="This attack does 70 damage for each Prize card you have taken.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)