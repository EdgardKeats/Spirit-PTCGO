from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6ba4f345-6bc1-5645-8558-7b6996823d4b",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Ability(
            title="Fiery Flapping",
            game_text="Once during your turn, if you have Articuno and Zapdos in play, you may use this Ability. Attach a Basic Fire Energy card from your hand to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)