from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a051fe28-fd7d-5f20-887b-5c62e516a224",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Ability(
            title="Flash-Pop Flapping",
            game_text="Once during your turn, if you have Moltres and Articuno in play, you may use this Ability. Attach a Basic Lightning Energy card from your hand to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Thundering Lightning",
            game_text="This Pok\u00e9mon also does 60 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=unimplemented,
        ),
    ],
)