from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c96c3ef0-daa4-5e27-84b2-cabd9eb9a9be",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachiex.Name",
    display_name="Jirachi ex",
    searchable_by=["Jirachi ex", "Basic", "ex", "Jirachiex"],
    subtypes=["Basic", "ex"],
    collector_number=102,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=385,
    abilities=[
        Attack(
            title="Wish Granter",
            game_text="Draw cards until you have 7 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=unimplemented,
        ),
    ],
)